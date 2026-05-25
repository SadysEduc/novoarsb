import discord
from discord.ext import commands
import json

with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']
AFK_INITIAL = config.get('afk', False)  # état initial AFK (True/False)

# Dictionnaire global pour stocker l’état AFK
afk_status = {
    "enabled": AFK_INITIAL
}

async def setup(bot):
    @bot.command()
    async def afk(ctx, state: str):
        state = state.lower()
        if state == "on":
            afk_status["enabled"] = True
            try:
                await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Afk]({WEBSITE})**
{THEME} **Afk:** Mode AFK activé
""")
            except:
                print("error afk")
        elif state == "off":
            afk_status["enabled"] = False
            try:
                await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Afk]({WEBSITE})**
{THEME} **Afk:** Mode AFK désactivé
""")
            except:
                print("error except afk")
        else:
            try:
                await ctx.message.edit(content="Utilise : afk on / afk off")
            except:
                await ctx.message.edit(content="Utilise : afk on / afk off")

