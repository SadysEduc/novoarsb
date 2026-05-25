import json
import random
import re

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def roll(ctx, dice: str = "1d6"):
        match = re.match(r'^\s*(\d{1,2})d(\d{1,4})\s*$', dice.lower())
        if not match:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Roll]({WEBSITE})**
{THEME} Format invalide. Exemple: `2d20`""")
            return

        count = int(match.group(1))
        faces = int(match.group(2))
        if count < 1 or count > 20 or faces < 2 or faces > 1000:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Roll]({WEBSITE})**
{THEME} Limites: 1-20 des, 2-1000 faces.""")
            return

        values = [random.randint(1, faces) for _ in range(count)]
        total = sum(values)
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Roll]({WEBSITE})**
{THEME} Lancers (`{count}d{faces}`): {', '.join(map(str, values))}
{THEME} Total: **{total}**""")
