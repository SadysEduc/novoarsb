import json
import random
import string

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)

NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']

_ALPHABET = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}."


async def setup(bot):
    @bot.command()
    async def password(ctx, length: int = 16):
        if length < 8 or length > 64:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Password]({WEBSITE})**
{THEME} Longueur invalide. Choisis entre 8 et 64.""")
            return

        generated = "".join(random.choice(_ALPHABET) for _ in range(length))
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Password]({WEBSITE})**
{THEME} Mot de passe ({length}): `{generated}`""")

