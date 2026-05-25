import base64
import json

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def b64encode(ctx, *, text: str):
        encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - B64Encode]({WEBSITE})**
{THEME} `{encoded}`""")

