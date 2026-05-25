import discord
from discord.ext import commands
import json
import asyncio

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
    async def utility(ctx):
            settings_msg = f"""
{THEME} **[❃ {NAME} ❃ - Utility]({WEBSITE})**
{THEME} `{PREFIX}avatar <user>` -> Avatar de l'utilisateur
{THEME} `{PREFIX}serverinfo <id>` -> Informations serveur
{THEME} `{PREFIX}ping` -> Latence du bot
{THEME} `{PREFIX}userinfo <user>` -> Informations utilisateur
{THEME} `{PREFIX}massdel <number>` -> Supprime des messages
{THEME} `{PREFIX}snipe <@user>` -> Snipe des messages
{THEME} `{PREFIX}massdm <message>` -> Envoi message a tous les amis
{THEME} `{PREFIX}nitrocheck <lien>` -> Verification nitro
{THEME} `{PREFIX}calc <expression>` -> Calculatrice securisee
{THEME} `{PREFIX}choose <a | b | c>` -> Choix aleatoire
{THEME} `{PREFIX}coinflip` -> Pile ou face
{THEME} `{PREFIX}roll <XdY>` -> Lance des des
{THEME} `{PREFIX}reverse <texte>` -> Inverse un texte
{THEME} `{PREFIX}uppercase <texte>` -> Texte en majuscules
{THEME} `{PREFIX}lowercase <texte>` -> Texte en minuscules
{THEME} `{PREFIX}textstats <texte>` -> Statistiques du texte
{THEME} `{PREFIX}uuidgen` -> Genere un UUID v4
{THEME} `{PREFIX}hashtext [algo] <texte>` -> Hash (sha256 par defaut)
{THEME} `{PREFIX}b64encode <texte>` -> Encode en Base64
{THEME} `{PREFIX}b64decode <base64>` -> Decode Base64
{THEME} `{PREFIX}now` -> Date/heure locale + UTC
{THEME} `{PREFIX}password [longueur]` -> Mot de passe aleatoire
        """
        await ctx.message.edit(content=settings_msg)

...
