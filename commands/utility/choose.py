import json
import random

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def choose(ctx, *, options: str):
        parsed = [part.strip() for part in options.replace(",", "|").split("|") if part.strip()]
        if len(parsed) < 2:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Choose]({WEBSITE})**
{THEME} Donne au moins 2 choix. Exemple: `choix1 | choix2 | choix3`""")
            return

        selected = random.choice(parsed)
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Choose]({WEBSITE})**
{THEME} Choix retenu: **{selected}**""")
