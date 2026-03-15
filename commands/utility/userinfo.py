import discord
from discord.ext import commands
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
    async def userinfo(ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author  # Si aucun membre n'est mentionné, prendre l'auteur du message

        user_info = (
            f"{THEME} **[❃ {NAME} ❃ - UserInfo]({WEBSITE})**\n"
            f"{THEME} **Utilisateur :** {member}\n"
            f"{THEME} **Discriminateur :** {member.discriminator}\n"
            f"{THEME} **ID :** {member.id}\n"
            f"{THEME} **Création du compte ** {member.created_at.strftime('%d/%m/%Y à %H:%M:%S')}\n"
            f"{THEME} **Serveur rejoint le :** {member.joined_at.strftime('%d/%m/%Y à %H:%M:%S')}\n"
            f"{THEME} **Rôles :** {', '.join([role.name for role in member.roles if role.name != '@everyone'])}\n"
            f"{THEME} **Status :** {member.status}\n"
            f"{THEME} **Activité :** {member.activity.name if member.activity else 'Aucune'}"
            f"{THEME} **Avatar :** {member.avatar.url}"
        )

        await ctx.message.edit(content=user_info)