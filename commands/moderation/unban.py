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
    async def unban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.unban(reason=reason)
            await ctx.send(content=f"""
{THEME} **[❃ {NAME} ❃ - UnBan]({WEBSITE})**
{THEME} **Utilisateur:** {member.mention}
{THEME} **Raison:** {reason if reason else 'None'}""")
        except discord.Forbidden:
            await ctx.send(content=f"""
{THEME} **[❃ {NAME} ❃ - UnBan]({WEBSITE})**
{THEME} **Utilisateur:** {member.mention}
{THEME} **Erreur:** No Permission""")
        except Exception as e:
            await ctx.send(content=f"""
{THEME} **[❃ {NAME} ❃ - UnBan]({WEBSITE})**
{THEME} **Erreur:** {type(e).__name__} - {e}""")