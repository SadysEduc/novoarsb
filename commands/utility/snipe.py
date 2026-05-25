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

deleted_messages = {}
    
async def setup(bot):
    @bot.event
    async def on_message_delete(message):
        if message.author.bot:
            return  
        if message.author not in deleted_messages:
            deleted_messages[message.author] = []

        deleted_messages[message.author].append(message.content)
        if len(deleted_messages[message.author]) > 3:  # Garde seulement les 3 derniers messages
            deleted_messages[message.author].pop(0)

    @bot.command()
    async def snipe(ctx, user: discord.User):
        if user in deleted_messages:
            messages = "\n".join(f"{THEME} ``{msg}``" for msg in deleted_messages[user])
            response = f"{THEME} **[❃ {NAME} ❃ - Snipe]({WEBSITE})**\n"
            response += f"{THEME} **Utilisateur:** {user.mention}\n"
            response += f"{THEME} **Derniers messages:**\n"
            response += messages
            await ctx.message.edit(content=response)
        else:
            await ctx.send(f"""
            {THEME} **[❃ {NAME} ❃ - Snipe]({WEBSITE})**
            {THEME} **Aucun message supprimé pour:** {user.mention}.""")