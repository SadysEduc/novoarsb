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
    async def settings(ctx):
            settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Settings]({WEBSITE})**
{THEME} 🌀 ``{PREFIX}Reboot`` ➜ Redémare le SB
{THEME} 🦚 ``{PREFIX}SetPrefix`` ➜ Change le préfix du SB
{THEME} 🩲 ``{PREFIX}Afk <on/off>`` ➜ Active/Désactive le mode AFK
{THEME} 🩲 ``{PREFIX}Rpc <type> <status> ou <jeux>`` ➜ Change le status du SB
            """
            await ctx.message.edit(content=settings_msg)