import discord
from discord.ext import commands
import json
import asyncio

with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix'] # suce ma bite DT <3
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']

async def setup(bot):
    @bot.command()
    async def nuke(ctx):
    # Avertir l'utilisateur des conséquences de cette commande
        await ctx.send(f"{THEME} **[❃ {NAME} ❃ - Nuke]({WEBSITE})**")
        await ctx.send(f"{THEME} **Nuked:** GoodBye Server :)")

    # Supprimer tous les salons et catégories de manière concurrente
        delete_channel_tasks = []
        for channel in ctx.guild.channels:
            delete_channel_tasks.append(channel.delete())

    # Supprimer tous les rôles de manière concurrente
        delete_role_tasks = []
        for role in ctx.guild.roles:
            if role != ctx.guild.default_role:  # Ne pas supprimer le rôle @everyone
                delete_role_tasks.append(role.delete())

    # Exécuter toutes les tâches de suppression de manière concurrente
        await asyncio.gather(*delete_channel_tasks)
        await asyncio.gather(*delete_role_tasks)