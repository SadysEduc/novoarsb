import json
import discord
from discord.ext import commands

with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']

def load_apps_config():
    with open('rpc_config.json', 'r') as f:
        return json.load(f)

async def setup(bot):
    @bot.command()
    async def rpc(ctx, mode: str = None, *, message: str = None):
        if not mode:
            await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - SetStatus]({WEBSITE})**\n"
                                           f"{THEME} Utilisation: `.rpc custom <type> <titre>` ou `.rpc <jeu>` ou `.rpc list`")
            return

        mode = mode.lower()
        apps = load_apps_config()

        if mode == "custom":
            if not message:
                await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - SetStatus]({WEBSITE})**\n"
                                               f"{THEME} Usage: `.rpc custom <playing|watching|listening|streaming> <titre>`")
                return

            try:
                stype, *title_parts = message.split(" ")
                title = " ".join(title_parts)
            except Exception:
                await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - SetStatus]({WEBSITE})**\n"
                                               f"{THEME} Usage invalide.")
                return

            stype = stype.lower()
            if stype not in ["playing", "watching", "listening", "streaming"]:
                await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - SetStatus]({WEBSITE})**\n"
                                               f"{THEME} Type invalide. Utilise : `playing`, `watching`, `listening`, `streaming`")
                return

            if stype == "playing":
                await bot.change_presence(activity=discord.Game(name=title))
            elif stype == "watching":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=title))
            elif stype == "listening":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=title))
            elif stype == "streaming":
                await bot.change_presence(activity=discord.Streaming(name=title, url="https://twitch.tv/discord"))

            await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - SetStatus]({WEBSITE})**\n"
                                           f"{THEME} Statut mis à jour : `{stype}` → **{title}**")

        elif mode == "list":
            app_list = ", ".join(f"`{app}`" for app in apps.keys())
            await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - Liste des statuts prédéfinis]({WEBSITE})**\n"
                                           f"{THEME} {app_list}")

        elif mode in apps:
            app = apps[mode]

            activity_type = {
                "playing": discord.ActivityType.playing,
                "watching": discord.ActivityType.watching,
                "listening": discord.ActivityType.listening,
                "streaming": discord.ActivityType.streaming
            }.get(app.get("type", "playing").lower(), discord.ActivityType.playing)

            if app.get("application_id"):
                activity = discord.Activity(
                    type=activity_type,
                    name=app.get("name", "Unknown"),
                    application_id=app.get("application_id"),
                    details=app.get("details"),
                    state=app.get("state"),
                    # Note: discord.py ne supporte pas les assets custom dans Activity, ce serait côté API Discord uniquement
                )
            else:
                # Pas d'app ID, on fait simple
                if activity_type == discord.ActivityType.playing:
                    activity = discord.Game(name=app.get("name", "Unknown"))
                else:
                    activity = discord.Activity(type=activity_type, name=app.get("name", "Unknown"))

            await bot.change_presence(activity=activity)

            await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - SetStatus]({WEBSITE})**\n"
                                           f"{THEME} Statut prédéfini activé : **{app.get('name', mode)}**")

        else:
            await ctx.message.edit(content=f"{THEME} **[❃ {NAME} ❃ - SetStatus]({WEBSITE})**\n"
                                           f"{THEME} Commande ou jeu inconnu. Utilise `.rpc list` pour voir les statuts prédéfinis.")
