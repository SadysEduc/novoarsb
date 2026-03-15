import discord
from discord.ext import commands
import json
import random

with open('config.json', 'r') as f:
    config = json.load(f)

THEME = config["theme"]
NAME = config["name"]
WEBSITE = config["website"]

async def setup(bot):
    @bot.command()
    async def toxicity(ctx, user: discord.Member = None):
        target = user or ctx.author
        toxic_percent = round(random.uniform(0.1, 100.0), 2)

        if toxic_percent >= 90:
            note = "☣️ Toxique extrême, à bannir direct."
        elif toxic_percent >= 70:
            note = "⚠️ Très toxique, attention à lui."
        elif toxic_percent >= 40:
            note = "🟡 Moyennement toxique."
        elif toxic_percent >= 20:
            note = "🟢 Légèrement toxique."
        else:
            note = "✅ Utilisateur sain, RAS."

        await ctx.message.edit(content=f"""{THEME} **[❃ {NAME} ❃ - Toxicity Scanner]({WEBSITE})**
👤 Utilisateur : {target.mention}
☠️ Niveau de toxicité : **{toxic_percent}%**
📋 Statut : {note}""")
