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
    async def banall(ctx):
    
        await ctx.send(f"{THEME} **[❃ {NAME} ❃ - BanAll]({WEBSITE})**")
        await ctx.send(f"**Banned:** GoodBye Members :)")

    # Parcourir tous les membres du serveur
        for member in ctx.guild.members:
            if member != ctx.guild.owner and not member.bot:  # Ne pas bannir le propriétaire du serveur ni les bots
                try:
                    await member.ban(reason="Banned by banall command")
                    await ctx.send(f'Banned {member.name}')
                except discord.Forbidden:
                    await ctx.send(f'Failed to ban {member.name}')
                except discord.HTTPException:
                    await ctx.send(f'HTTP Exception when trying to ban {member.name}')