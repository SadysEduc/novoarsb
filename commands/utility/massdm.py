import discord
from discord.ext import commands
import asyncio
import json




with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']


async def setup(bot):
    @bot.command()
    async def massdm(ctx, *, message: str):
        try:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Aic]({WEBSITE})**
{THEME} **MassDM:** Envoi des messages... <a:loading:1389355080217526273>""")
        except Exception:
            pass  # Certains messages ne peuvent pas être édités en selfbot

        sent_count = 0
        failed_count = 0

        # Envoi aux amis
        if hasattr(bot.user, 'friends'):
            friends = bot.user.friends
            for friend in friends:
                try:
                    dm = await friend.create_dm()
                    await dm.send(message)
                    sent_count += 1
                except Exception:
                    failed_count += 1
                await asyncio.sleep(10)  # cooldown systématique

        try:
            await ctx.author.send(
                f"""{THEME} **[❃ {NAME} ❃ - Aic]({WEBSITE})**
                {THEME} **MassDM:** MassDM terminé. Envoyés : {sent_count}\nÉchecs : {failed_count} <a:success:1389362166284685516>""")
        except:
            pass
