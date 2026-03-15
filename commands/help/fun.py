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
    async def fun(ctx):
        settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Fun]({WEBSITE})**
{THEME} 🔞 ``{PREFIX}Branlette`` ➜ Envoie une animation de masturbation
{THEME} 😘 ``{PREFIX}Kiss @user`` ➜ Fait un bisous à l'utilisateur mentionné
{THEME} 💖 ``{PREFIX}Love @user`` ➜ Envoie des coeurs à l'utilisateur mentionné
{THEME} 🖐️ ``{PREFIX}Slap @user`` ➜ Envoie une claque à l'utilisateur mentionné
{THEME} 💻 ``{PREFIX}Hack @user`` ➜ Pirate l'utilisateur mentionné
{THEME} ☣️ ``{PREFIX}Toxicity @user`` ➜ Scanne la toxicité RP de l'utilisateur
{THEME} 💬 ``{PREFIX}Say @user <message>`` ➜ Envoie un message via webhook imitant un utilisateur
{THEME} 🍒 ``{PREFIX}Boobs @user`` ➜ Donne la tailles des cerise de l'utiliseur
{THEME} 🚓 ``{PREFIX}Fbi @user`` ➜ Affiche le niveau de recherche du FBI de l'utiliseur
{THEME} 👤 ``{PREFIX}Pp @user`` ➜ Donne la taille de la baguette de l'utilisateur

"""
        await ctx.message.edit(content=settings_msg)