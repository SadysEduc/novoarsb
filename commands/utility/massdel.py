import discord
from discord.ext import commands
import json
import asyncio

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)


TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']

async def setup(bot):
    @bot.command()
    async def massdel(ctx):
        await ctx.message.edit(f"""
        {THEME} **[❃ {NAME} ❃ - MassDel]({WEBSITE})**
        {THEME} **Erreur:** Message.delete() missing arguments ()""")  