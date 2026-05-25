import discord
from discord.ext import commands
import json
import os
import asyncio
from datetime import datetime

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
    async def sadys(ctx):
        settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Sadys]({WEBSITE})**
{THEME} ❤️ ``{PREFIX}HeartLog <message|list>`` ➜ Journaliser tes souvenirs ou peine...
{THEME} 🔥 ``{PREFIX}HeartBurn`` ➜ Effacer ton cœur numérique 
{THEME} 💔 ``{PREFIX}LostLove`` ➜ uhm....
{THEME} 💔 ``{PREFIX}SinceBreak`` ➜ Sa me fait toujours mal...
{THEME} 🧠 ``{PREFIX}Citation`` ➜ Balance une citation
        """
        await ctx.message.edit(content=settings_msg)