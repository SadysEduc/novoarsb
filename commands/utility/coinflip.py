import json
import random

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def coinflip(ctx):
        result = random.choice(["Pile", "Face"])
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - CoinFlip]({WEBSITE})**
{THEME} Resultat: **{result}**""")

