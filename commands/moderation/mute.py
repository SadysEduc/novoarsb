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
    async def mute(ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        muted_role = discord.utils.get(guild.roles, name="Muted")

        if not muted_role:
            try:
                # Si le rôle "Muted" n'existe pas, le créer
                muted_role = await guild.create_role(name="Muted")

                for channel in guild.channels:
                    await channel.set_permissions(muted_role, speak=False, send_messages=False, read_message_history=True, read_messages=False)

            except discord.Forbidden:
                # Gestion de l'erreur si le bot n'a pas la permission de créer un rôle ou de modifier les permissions des canaux
                await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Mute]({WEBSITE})**
{THEME} **Utilisateur:** {member.mention} 
{THEME} **Erreur:** No Permission""")
                return

        try:
            await member.add_roles(muted_role, reason=reason)
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Mute]({WEBSITE})**
{THEME} **Utilisateur:** {member.mention} 
{THEME} **Raison:** {reason}""")
            
        except discord.Forbidden:
            # Gestion de l'erreur si le bot n'a pas la permission d'ajouter le rôle à l'utilisateur
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Mute]({WEBSITE})**
{THEME} **Utilisateur:** {member.mention} 
{THEME} **Erreur:** No Permission""")
            
        except Exception as e:
            # Gestion de toutes les autres erreurs inattendues
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Mute]({WEBSITE}) 
{THEME} **Erreur:** {type(e).__name__} - {e}""")
        finally:
            pass
