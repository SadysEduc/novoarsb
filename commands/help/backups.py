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
    async def backups(ctx):
            backups = f"""
{THEME} **[❃ {NAME} ❃ - Backups]({WEBSITE})**
{THEME} 🚍 ``{PREFIX}Backup create `` ➜ Crée une nouvelle backup
{THEME} 🚍 ``{PREFIX}Backup load <id>`` ➜ Charge une backup
{THEME} 🚍 ``{PREFIX}Backup list`` ➜ Affiche la liste des backups
            """
            await ctx.message.edit(content=backups)