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
    async def utility(ctx):
            settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Utility]({WEBSITE})**
{THEME} 👓 ``{PREFIX}Avatar <user>`` ➜ Envoie avatar de lutilisateur
{THEME} 🧾 ``{PREFIX}Serverinfo <id>`` ➜ Affiche les informations du serveur
{THEME} 📌 ``{PREFIX}Ping`` ➜ Affiche la latence du bot
{THEME} 📊 ``{PREFIX}Userinfo <user>`` ➜ Envoie les informations concernant l'utilisateur mentionné
{THEME} 🎑 ``{PREFIX}Massdel <number>`` ➜ Supprimes des messages
{THEME} 🏹 ``{PREFIX}Snipe <@user>`` ➜ Snipe les deux derniers messages de l'utilisateur 
{THEME} 🚔 ``{PREFIX}MassDm <message>`` ➜ Envoie un message à tous les amis de l'utilisateur
{THEME} 🦚 ``{PREFIX}NitroCheck <lien> `` ➜ Vérifie si le nitro est valide 
            """
            await ctx.message.edit(content=settings_msg)
