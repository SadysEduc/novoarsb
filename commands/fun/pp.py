import discord
from discord.ext import commands
import json
import random

async def setup(bot):
    with open('config.json') as f:
        config = json.load(f)

    THEME = config["theme"]
    NAME = config["name"]
    WEBSITE = config["website"]

    @bot.command()
    async def pp(ctx, user: discord.Member = None):
        user = user or ctx.author

        # Génére une "taille" de PP (stable par user.id)
        random.seed(user.id)
        size = random.randint(0, 20)
        emoji = "8"

        # Visualisation RP
        bar = f"{emoji}" + ("=" * size) + "D"

        # Thème + embed stylé
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - PP Scanner]({WEBSITE})**
{THEME} 👤 Utilisateur: `{user.display_name}`
{THEME} 📏 Taille de la baguette: `{size}cm`
{THEME} `{bar}`
""")
