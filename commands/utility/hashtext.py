import hashlib
import json

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']

_ALGORITHMS = {"md5", "sha1", "sha224", "sha256", "sha384", "sha512"}


async def setup(bot):
    @bot.command()
    async def hashtext(ctx, *, payload: str):
        parts = payload.split(" ", 1)
        algo = "sha256"
        text = payload

        if len(parts) == 2 and parts[0].lower() in _ALGORITHMS:
            algo = parts[0].lower()
            text = parts[1]

        digest = hashlib.new(algo, text.encode("utf-8")).hexdigest()
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - HashText]({WEBSITE})**
{THEME} Algo: **{algo}**
{THEME} Hash: `{digest}`""")

