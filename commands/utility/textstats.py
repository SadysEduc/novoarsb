import json

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def textstats(ctx, *, text: str):
        words = len(text.split())
        chars = len(text)
        chars_no_space = len(text.replace(" ", ""))
        lines = text.count("\n") + 1

        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - TextStats]({WEBSITE})**
{THEME} Mots: **{words}**
{THEME} Caracteres: **{chars}**
{THEME} Caracteres (sans espaces): **{chars_no_space}**
{THEME} Lignes: **{lines}**""")

