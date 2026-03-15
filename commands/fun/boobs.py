import discord
from discord.ext import commands
import json
import random

with open('config.json') as f:
    config = json.load(f)

THEME = config["theme"]
NAME = config["name"]
WEBSITE = config["website"]

tailles = [
    "🚫 Rien du tout",
    "🍒 Mini",
    "🍑 Petit plaisir",
    "🍈 Moyenne douce",
    "🥥 Respectable",
    "🍉 Tchernobyl",
    "🛢️ Gigamax",
    "📦 Trop pour être humain"
]

async def setup(bot):

    @bot.command()
    async def boobs(ctx, user: discord.Member = None):
        target = user or ctx.author
        taille = random.choice(tailles)

        await ctx.message.edit(content=f"""{THEME} **[❃ {NAME} ❃ - Boobs Scanner]({WEBSITE})**
{THEME} 👤 Utilisateur : {target.mention}
{THEME} 📏 Taille détectée : **{taille}**""")
