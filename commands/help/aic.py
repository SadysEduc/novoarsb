import discord
from discord.ext import commands
import json
import asyncio

with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']
    

async def setup(bot):
    @bot.command()
    async def aic(ctx):
            settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Aic]({WEBSITE})**
{THEME} 💬 ``{PREFIX}Ai <message>`` ➜ Demande quelque chose à l'ia
{THEME} 🚔 ``{PREFIX}Cars <fichier.mp4/avi/...>`` ➜ Analyse la vidéo pour détecter des voitures         """
            await ctx.message.edit(content=settings_msg)
            