import discord
from discord.ext import commands
import json
import random

with open('config.json') as f:
    config = json.load(f)

THEME = config["theme"]
NAME = config["name"]
WEBSITE = config["website"]

statuses = [
    "✅ Aucune anomalie détectée.",
    "⚠️ Surveillance active en cours.",
    "🚨 Suspect lié à des activités louches.",
    "🚫 Fiché S par le FBI.",
    "🟠 Dossier en cours d'analyse.",
    "🔴 Recherche internationale en cours.",
    "👮‍♂️ Mandat d'arrêt signé.",
    "📂 Classé top secret : danger public.",
]

async def setup(bot):

    @bot.command()
    async def fbi(ctx, user: discord.Member = None):
        target = user or ctx.author
        status = random.choice(statuses)

        await ctx.message.edit(content=f"""{THEME} **[❃ {NAME} ❃ - FBI CHECK]({WEBSITE})**
{THEME} 👤 Cible: {target.mention}
{THEME} 🔎 Statut: **{status}**""")
