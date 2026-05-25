import discord
from discord.ext import commands
import json
import random

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)


TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']

love_animations = [
    "https://i.pinimg.com/originals/dc/9b/43/dc9b433cdd102f690521646c7562cdf9.gif",
    "https://media.tenor.com/PGXshKPAUh4AAAAM/my-dress-up-darling-anime-love.gif",
    "https://i.pinimg.com/originals/0c/10/f5/0c10f57696e4507eb1d05c6bc2b988f9.gif",
    "https://i.gifer.com/FqfH.gif You have found the Easter Eggs !",
    "https://i.pinimg.com/originals/11/0d/bd/110dbddfd3d662479c214cacb754995d.gif",
    "https://gifsec.com/wp-content/uploads/2022/11/love-anime-gif-43.giff",
    "https://25.media.tumblr.com/090a17b85a7b6a35dea80a6e62550e5f/tumblr_mo5jwhNuYn1s4dyyio1_500.gif"
]


async def setup(bot):
    @bot.command()
    async def love(ctx, *, user: discord.User):
        love = random.choice(love_animations)
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Love]({WEBSITE})**
{THEME} {ctx.author.mention} Fait un bisous à {user.mention}
{THEME} **Gif:** {love}""")