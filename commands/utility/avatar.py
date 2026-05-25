from discord.ext import commands
import json
import discord
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
    async def avatar(ctx, user: discord.User):
        try:
            avatar_url = user.avatar.url
            avatarmsg = f"{THEME} **[❃ {NAME} ❃ - Avatar]({WEBSITE})**\n {THEME} **Avatar:** {avatar_url}"
            await ctx.send(avatarmsg)

        except Exception as e:
            await ctx.message.edit(content=f"""
            {THEME} **[❃ {NAME} ❃ - Avatar]({WEBSITE})
            {THEME} **Erreur:** {str(e)}""")


