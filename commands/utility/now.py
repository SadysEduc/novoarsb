import json
from datetime import datetime, timezone

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def now(ctx):
        local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        utc_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Now]({WEBSITE})**
{THEME} Local: **{local_time}**
{THEME} UTC: **{utc_time}**""")

