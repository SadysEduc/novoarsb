import discord
from discord.ext import commands
import asyncio
import os
import time
import json
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO('yolov5s.pt')  # Charge le modèle au niveau global
# Chargement de la configuration
with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
THEME = config['theme']
DELTIME = config['deltime']
WEBSITE = config['website']


async def setup(bot):

    @bot.command()
    async def cars(ctx):

        if not ctx.message.attachments:
            await ctx.send(f"{THEME} **[❃ {NAME} ❃ - Cars]({WEBSITE})**\n{THEME} **Erreur:** Vous devez joindre une vidéo.")
            return

        attachment = ctx.message.attachments[0]
        if not attachment.filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            await ctx.send(f"{THEME} **[❃ {NAME} ❃ - Cars]({WEBSITE})**\n{THEME} **Erreur:** Le fichier doit être une vidéo.")
            return

        await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - Cars]({WEBSITE})**\n{THEME} **Téléchargement de la vidéo...**")

        video_path = f"{int(time.time())}_{attachment.filename}"
        await attachment.save(video_path)

        await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - Cars]({WEBSITE})**\n{THEME} **Traitement en cours...**")

        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        if not ret:
            await ctx.send(f"{THEME} **[❃ {NAME} ❃ - Cars]({WEBSITE})**\n{THEME} **Erreur:** Impossible de lire la vidéo.")
            cap.release()
            os.remove(video_path)
            return

        height, width, _ = frame.shape
        fps = cap.get(cv2.CAP_PROP_FPS)
        if not fps or fps <= 0:
            fps = 30

        output_path = f"processed_{int(time.time())}.avi"
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        if not out.isOpened():
            await ctx.send(f"{THEME} **[❃ {NAME} ❃ - Cars]({WEBSITE})**\n{THEME} **Erreur:** Impossible d'initialiser le VideoWriter.")
            cap.release()
            os.remove(video_path)
            return

        prev_positions = {}
        car_id_counter = 0
        car_speeds = {}

        def get_centroid(box):
            x1, y1, x2, y2 = box
            return (int((x1 + x2) / 2), int((y1 + y2) / 2))

        frame_index = 0

        while True:
            if frame_index != 0:
                ret, frame = cap.read()
                if not ret:
                    break
            frame_index += 1

            results = model(frame)[0]

            vehicles = []
            for box, conf, cls in zip(results.boxes.xyxy, results.boxes.conf, results.boxes.cls):
                cls = int(cls)
                if cls in [2, 3, 5, 7] and conf > 0.5:
                    vehicles.append(box.cpu().numpy())

            current_positions = []
            for box in vehicles:
                x1, y1, x2, y2 = map(int, box)
                centroid = get_centroid((x1, y1, x2, y2))
                current_positions.append(((x1, y1, x2, y2), centroid))

            matched = {}
            used_prev_ids = set()

            for box, centroid in current_positions:
                best_id = None
                best_dist = 1e9
                for car_id, prev_centroid in prev_positions.items():
                    dist = np.linalg.norm(np.array(centroid) - np.array(prev_centroid))
                    if dist < 50 and car_id not in used_prev_ids:
                        if dist < best_dist:
                            best_dist = dist
                            best_id = car_id
                if best_id is None:
                    car_id_counter += 1
                    best_id = car_id_counter
                matched[best_id] = centroid
                used_prev_ids.add(best_id)

                if best_id in prev_positions:
                    dx = centroid[0] - prev_positions[best_id][0]
                    dy = centroid[1] - prev_positions[best_id][1]
                    dist_px = (dx*dx + dy*dy)**0.5
                    speed_px_per_frame = dist_px
                    speed_kmh = speed_px_per_frame * fps * 0.1  # facteur à calibrer
                    car_speeds[best_id] = speed_kmh
                else:
                    car_speeds[best_id] = 0

                x1, y1, x2, y2 = box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                speed_text = f"{int(car_speeds[best_id])} km/h"
                cv2.putText(frame, speed_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            prev_positions = matched

            out.write(frame)

            if frame_index % 30 == 0:
                await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - Cars]({WEBSITE})**\n{THEME} **Traitement en cours... {frame_index} frames traitées**")

        cap.release()
        out.release()

        await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - Cars]({WEBSITE})**\n{THEME} **Upload de la vidéo traitée...**")

        await ctx.send(file=discord.File(output_path))

        try:
            os.remove(video_path)
            os.remove(output_path)
            await asyncio.sleep(DELTIME)
            await ctx.message.delete()
        except Exception:
            pass
