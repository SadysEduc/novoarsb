import json

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def uppercase(ctx, *, text: str):
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Uppercase]({WEBSITE})**
{THEME} {text.upper()}""")

