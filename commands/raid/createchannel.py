from discord.ext import commands
import json
import asyncio
import random
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
    async def createchannel(ctx):
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - CreateChannel]({WEBSITE})**
{THEME} **CreateChannel:** Hello #Raid-By-Novoar-Selfbot-15 : )""")
    # Créer les salons
        created_channels = []
        for i in range(100):
            num = random.randint(1, 120)  
            channel = await ctx.guild.create_text_channel(name=f"Raid-By-{NAME}-{num}")
            created_channels.append(channel)
            await asyncio.sleep(0.1)  # Attendre un peu entre les créations de salons pour éviter de surcharger l'API
