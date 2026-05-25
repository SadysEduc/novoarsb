import os
import json
import asyncio
import discord
from discord.ext import commands
from datetime import datetime

with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']
def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def save_config(data):
    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4)

async def setup(bot):
    @bot.command()
    async def setprefix(ctx, newpref: str):
        config = load_config()
        config['prefix'] = newpref
        save_config(config)
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - SetPrefix]({WEBSITE})**
{THEME} **SetPrefix:** Préfix changé sur ``{newpref}`` avec succès!""")
