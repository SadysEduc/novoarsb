import base64
import binascii
import json

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def b64decode(ctx, *, payload: str):
        try:
            decoded = base64.b64decode(payload.encode("utf-8"), validate=True).decode("utf-8")
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - B64Decode]({WEBSITE})**
{THEME} `{decoded}`""")
        except (binascii.Error, UnicodeDecodeError):
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - B64Decode]({WEBSITE})**
{THEME} Base64 invalide.""")

