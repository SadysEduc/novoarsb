import discord
from discord.ext import commands
import os
import json
import time

# Chargement de la config
with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
GENIUS_TOKEN = config['genius_token']
THEME = config['theme']
WEBSITE = config['website']

# Dossier des backups
BACKUP_DIR = "backups"
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# Setup pour chargement dynamique
async def setup(bot):
    @bot.command()
    async def backup(ctx, action=None, backup_id=None):
        if action == "create":
            await create_backup(ctx)
        elif action == "list":
            await list_backups(ctx)
        elif action == "load" and backup_id:
            await load_backup(ctx, backup_id)
        else:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Backup]({WEBSITE})**
{THEME} **Erreur:** Utilisation : `.backup create`, `.backup list`, `.backup load <id>`""")

    async def create_backup(ctx):
        guild = ctx.guild
        backup_data = {
            "name": guild.name,
            "icon": str(guild.icon.url) if guild.icon else None,
            "roles": [],
            "channels": []
        }

        for role in guild.roles:
            if role.is_default():
                continue
            backup_data["roles"].append({
                "name": role.name,
                "color": role.color.value,
                "permissions": role.permissions.value,
                "position": role.position,
                "mentionable": role.mentionable,
                "hoist": role.hoist
            })

        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                backup_data["channels"].append({
                    "name": channel.name,
                    "type": "text",
                    "category": channel.category.name if channel.category else None,
                    "position": channel.position,
                    "topic": channel.topic
                })
            elif isinstance(channel, discord.VoiceChannel):
                backup_data["channels"].append({
                    "name": channel.name,
                    "type": "voice",
                    "category": channel.category.name if channel.category else None,
                    "position": channel.position,
                    "bitrate": channel.bitrate,
                    "user_limit": channel.user_limit
                })

        backup_id = str(int(time.time()))
        with open(f"{BACKUP_DIR}/{backup_id}.json", "w", encoding="utf-8") as f:
            json.dump(backup_data, f, indent=4)

        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Backup]({WEBSITE})**
{THEME} **Backup:** Créée avec succès ! ID : ``{backup_id}``""")

    async def list_backups(ctx):
        files = os.listdir(BACKUP_DIR)
        if not files:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Backup]({WEBSITE})**
{THEME} **Backup:** Aucune backup trouvée.""")
            return

        backups = [f"📦 ``{f.replace('.json','')}``" for f in files if f.endswith(".json")]
        backup_list = "\n".join(backups)
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Backup]({WEBSITE})**
{THEME} **Backups disponibles :**\n{backup_list}""")

    async def load_backup(ctx, backup_id):
        path = f"{BACKUP_DIR}/{backup_id}.json"
        if not os.path.exists(path):
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Backup]({WEBSITE})**
{THEME} **Backup:** Introuvable avec l'ID ``{backup_id}``.""")
            return

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Backup]({WEBSITE})**
{THEME} **Backup:** Chargement de la backup ``{backup_id}``...""")

        await ctx.guild.edit(name=data["name"])

        for role_data in sorted(data["roles"], key=lambda x: x["position"]):
            await ctx.guild.create_role(
                name=role_data["name"],
                permissions=discord.Permissions(role_data["permissions"]),
                colour=discord.Colour(role_data["color"]),
                hoist=role_data["hoist"],
                mentionable=role_data["mentionable"]
            )

        for ch in ctx.guild.channels:
            try:
                await ch.delete()
            except:
                pass

        categories = {}
        for ch in data["channels"]:
            category_name = ch.get("category")
            if category_name and category_name not in categories:
                categories[category_name] = await ctx.guild.create_category(name=category_name)

            if ch["type"] == "text":
                await ctx.guild.create_text_channel(
                    name=ch["name"],
                    category=categories.get(category_name),
                    position=ch["position"],
                    topic=ch.get("topic")
                )
            elif ch["type"] == "voice":
                await ctx.guild.create_voice_channel(
                    name=ch["name"],
                    category=categories.get(category_name),
                    position=ch["position"],
                    bitrate=ch["bitrate"],
                    user_limit=ch["user_limit"]
                )

        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Backup]({WEBSITE})**
{THEME} **Backup:** Restaurée avec succès ! ✅""")
