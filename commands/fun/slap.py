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

slap_animations = [
    "https://gifdb.com/images/high/anime-kissing-498-x-280-gif-op3h5wkpm21z2dil.gif",
    "https://gifdb.com/images/high/up-close-angry-anime-slap-lf84tjs2sgx8obdr.gif",
    "https://i.pinimg.com/originals/b6/d8/a8/b6d8a83eb652a30b95e87cf96a21e007.gif",
    "https://gifdb.com/images/high/mad-girlfriend-intense-anime-slap-x5o3heygjpculnqb.gif",
    "https://gifdb.com/images/high/mad-anime-female-character-slap-0zljynqqf0gopfhg.gif",
    "https://i.chzbgr.com/full/8574231808/h50C257DD/oneslap-man",
    "https://mageinabarrel.com/wp-content/uploads/2014/06/akari-slap.gif"
]


async def setup(bot):
    @bot.command()
    async def slap(ctx, *, user: discord.User):
         slap = random.choice(slap_animations)
         await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Slap]({WEBSITE})**
{THEME} {ctx.author.mention} met une claque à {user.mention}
{THEME} **Gif:** {slap}
""")