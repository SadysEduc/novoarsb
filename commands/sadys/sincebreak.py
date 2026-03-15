import discord
from discord.ext import commands
import json
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
    async def sincebreak(ctx):
        break_date = datetime(2023, 3, 16)
        now = datetime.now()
        delta = now - break_date
        await ctx.message.edit(f"❤️ Il s'est écoulé **{delta.days} jours** depuis le 16.03.23...")    


