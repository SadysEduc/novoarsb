import discord
from discord.ext import commands
import json

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)


TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']

async def setup(bot):
    @bot.command()
    async def serverinfo(ctx, guild_id: int):
        try:
            guild = bot.get_guild(guild_id)
            if guild is None:
                await ctx.message.edit(content=f"""
                {THEME} **[❃ {NAME} ❃]({WEBSITE})**
                {THEME} Aucun serveur trouvé""")
                return
        
            owner = guild.owner
            vanity_link = guild.vanity_url_code
            boost_level = guild.premium_tier
            created_at = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
            verification_level = guild.verification_level
            roles = len(guild.roles)
            channels = len(guild.channels)
            servavatar = guild.icon
            bannerserv = guild.banner
        
            server_info_msg = f"""
{THEME} **[❃ {NAME} ❃ - ServerInfo]({WEBSITE})**
{THEME} **Propriétaire:** {owner}
{THEME} **Lien Vanity:** {vanity_link or 'Pas de lien Vanity'}
{THEME} **Niveau Nitro Boost:** {boost_level}
{THEME} **Créé le:** {created_at}
{THEME} **Niveau de vérification:** {verification_level}
{THEME} **Nombre de rôles:** {roles}
{THEME} **Nombre de salons:** {channels}
{THEME} **Avatar du serveur:** {servavatar}
{THEME} **Bannière du serveur:** {bannerserv}
            """
            await ctx.message.edit(content=server_info_msg)

        except Exception as e:
            await ctx.message.edit(content=f"""
            {THEME} **[❃ {NAME} ❃]({WEBSITE})**
            {THEME} Erreur: {e}""")