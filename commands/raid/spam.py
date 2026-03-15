from discord.ext import commands
import json
import discord
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
    async def spam(ctx):
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Spam]({WEBSITE})**
{THEME} **⚠️ MAINTENANCE ⚠️**""")
        
