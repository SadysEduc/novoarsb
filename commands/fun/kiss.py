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

kiss_animations = [
    "https://gifdb.com/images/high/anime-kissing-498-x-280-gif-op3h5wkpm21z2dil.gif",
    "https://www.icegif.com/wp-content/uploads/2022/10/icegif-1392.gif",
    "https://i.pinimg.com/originals/50/28/66/502866fc3e3722a3317507c503ab19c0.gif",
    "https://gifdb.com/images/high/anime-girl-flying-kiss-l8ydgpd7cdkxo1l6.gif",
    "https://25.media.tumblr.com/090a17b85a7b6a35dea80a6e62550e5f/tumblr_mo5jwhNuYn1s4dyyio1_500.gif",
    "https://media.tenor.com/fbZG_aG8So8AAAAi/anime-kissing.gif",
    "https://37.media.tumblr.com/6a4c261749e29a61882972e4018c01b1/tumblr_n2u9usvMQc1twud4zo1_500.gif"
]


async def setup(bot):
    @bot.command()
    async def kiss(ctx, *, user: discord.User):
        kiss_animation = random.choice(kiss_animations)
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Kiss]({WEBSITE})**
{THEME} {ctx.author.mention} Fait un bisous à {user.mention}
{THEME} **Gif:** {kiss_animation}""")