import discord
from discord.ext import commands
import asyncio
import random
import json
import os

# Chargement des variables depuis config.json
with open('config.json') as config_file:
    config = json.load(config_file)

THEME = config['theme']
NAME = config['name']
WEBSITE = config['website']

async def setup(bot):

    @bot.command()
    async def hack(ctx, user: discord.Member = None):
        if not user:
            await ctx.message.edit(content=f"""{THEME} **[❃ {NAME} ❃ - Hack]({WEBSITE})**
{THEME} **Erreur :** Mentionne une personne à hacker.""")
            return

        steps = [
            f"🔍 Recherche d'informations sur **{user.name}**...",
            "📡 Connexion au serveur distant...",
            f"📍 IP localisée : `{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}`",
            "📥 Téléchargement de l'historique Discord...",
            "🧬 Analyse des fichiers privés...",
            "🔓 Décryptage du mot de passe...",
            f"💉 Injection de RAT sur l'appareil de {user.name}...",
            "📤 Envoi des données vers le Dark Web...",
            "💣 Déploiement d’un virus...",
            f"✅ Hack de {user.mention} terminé avec succès."
        ]

        await ctx.message.edit(content=f"""{THEME} **[❃ {NAME} ❃ - Hack]({WEBSITE})**
{THEME} **Statut :** Lancement du hack de {user.mention}...""")

        for step in steps:
            await asyncio.sleep(random.uniform(1.1, 2.0))
            await ctx.message.edit(content=f"""{THEME} **[❃ {NAME} ❃ - Hack]({WEBSITE})**
{THEME} **Hacking:** {step}""")
