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

async def setup(bot):
    @bot.command()
    async def ping(ctx):
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Ping]({WEBSITE})**
{THEME} **Pong!** 12ms""")
