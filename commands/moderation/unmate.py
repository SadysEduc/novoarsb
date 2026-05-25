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
    async def unmute(ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        muted_role = discord.utils.get(guild.roles, name="Muted")

        if not muted_role:
            await ctx.send("Le rôle 'Muted' n'existe pas.")
            return

        if muted_role not in member.roles:
            await ctx.send(f"{member.mention} n'a pas le rôle 'Muted'.")
            return

        try:
            await member.remove_roles(muted_role, reason=reason)
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - UnMute]({WEBSITE})**
{THEME} **Utilisateur:** {member.mention} 
{THEME} **Raison:** {reason if reason else 'None'}""")
        
        except discord.Forbidden:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - UnMute]({WEBSITE})**
{THEME} **Utilisateur:** {member.mention} 
{THEME} **Erreur:** No Permission""")


        except Exception as e:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - UnMute]({WEBSITE}) 
{THEME} **Erreur:** {type(e).__name__} - {e}""")


        finally:
            pass
