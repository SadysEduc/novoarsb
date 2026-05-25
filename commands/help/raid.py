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
    async def raid(ctx):
            settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Raid]({WEBSITE})**
{THEME} 🚫 ``{PREFIX}BanAll`` ➜ Ban toutes les personnes du serveur
{THEME} 💣 ``{PREFIX}Nuke`` ➜ Supprimes touts les roles, salons du serveur
{THEME} 💻 ``{PREFIX}Spam`` ➜ Spam everyone dans tous les salons
{THEME} 🎰 ``{PREFIX}CreateChannel `` ➜  Créer pleins de salons
            """
            await ctx.message.edit(content=settings_msg)