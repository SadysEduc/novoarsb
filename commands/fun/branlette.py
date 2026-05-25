import discord
from discord.ext import commands
import json
import asyncio
import random

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
    async def branlette(ctx):
        base = "8=={}==D"
        hand_positions = [
            "8====✊D",
            "8===✊=D",
            "8==✊==D",
            "8=✊===D",
            "8✊====D",
            "8=✊===D",
            "8==✊==D",
            "8===✊=D",


        ]
    
    
        for _ in range(3):  # Repeat the animation 3 times
            for hand_position in hand_positions:
                await asyncio.sleep(0.001)
                await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Branlette]({WEBSITE})**
{THEME} **Branlette:** {hand_position}""")
                
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Branlette]({WEBSITE})**
{THEME} **Branlette:** 8====✊D💦""")