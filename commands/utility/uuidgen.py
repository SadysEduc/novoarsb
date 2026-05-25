import json
import uuid

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def uuidgen(ctx):
        value = str(uuid.uuid4())
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - UUID]({WEBSITE})**
{THEME} `{value}`""")

