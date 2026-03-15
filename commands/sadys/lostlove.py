import discord
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
    async def lostlove(ctx):
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - LostLove]({WEBSITE})**
{THEME} 💔 16.03.23 — Le jour où tout a changé.
{THEME} Parfois, on perd pas une simple personne, on perd un morceau de soi-même.
{THEME} C'était pas juste une date. C'était une partie de moi-même.... (Sadys. L'amour brise des vie...)
""")






