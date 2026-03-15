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
    async def moderation(ctx):
            settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Moderation]({WEBSITE})**
{THEME} 🚫 ``{PREFIX}Mute <user> `` ➜ Mute l'utilisateur mentionné
{THEME} 🗣️ ``{PREFIX}UnMute <user>`` ➜ Unmute l'utilisateur mentionné
{THEME} ⛔ ``{PREFIX}Ban <user> `` ➜ Ban l'utilisateur mentionné
{THEME} 🫡 ``{PREFIX}UnBan <user>`` ➜ UnBan l'utilisateur mentionné
"""
            await ctx.message.edit(content=settings_msg)