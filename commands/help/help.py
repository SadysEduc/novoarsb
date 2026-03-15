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
    async def help(ctx):
            settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Help]({WEBSITE})**
{THEME} 🤖 ``{PREFIX}Raid`` ➜ Catégorie Raid
{THEME} 🛠️ ``{PREFIX}Utility`` ➜ Catégorie Utility
{THEME} 🤠 ``{PREFIX}Fun`` ➜ Catégorie Fun
{THEME} 🔧 ``{PREFIX}Moderation`` ➜ Catégorie Moderation
{THEME} ⚙️ ``{PREFIX}Settings`` ➜ Paramètres du SelfBot
{THEME} ➕ ``{PREFIX}Pentest`` ➜ Catégorie Pentest
{THEME} 🧠 ``{PREFIX}Aic`` ➜ Catégorie Intelligence Artificielle
{THEME} 🧠 ``{PREFIX}Backups`` ➜ Catégorie Backups
{THEME} 🧠 ``{PREFIX}Sadys`` ➜ Catégorie assez spécial....
            """
            await ctx.message.edit(content=settings_msg)