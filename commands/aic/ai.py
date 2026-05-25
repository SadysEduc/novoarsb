import discord
from discord.ext import commands
import json
import ollama

# Chargement de la configuration
with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
THEME = config['theme']
WEBSITE = config['website']
MODEL = "MEGAN:latest"

# Message système d'identité
import datetime

SYSTEM_PROMPT = f"""
Tu es une intelligence artificielle intégrée au selfbot Discord **NovoarSB**.
Tu es un assistant personnel et tu parles exclusivement français.
Ton développeur est **Sadys**.

🔧 Version : 1.3.3 | Aucune mise à jour disponible.
📦 Modules actifs : utility, moderation, fun, pentest, settings, raid, help, intelligence artifficiel
📑 Commandes disponibles : 36
📌 Préfixe actuel : {PREFIX}
📋 Liste des commandes avec : ``{PREFIX}help``
👀 Serveur Discord : https://discord.gg/novoarsb
🕒 Dernier redémarrage : {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
🦚 Pour contacter le support il faut aller dans ce salon <#1389603109352771714>
🌀 Pour donner des suggestions il faut aller dans ce salon <#1389079567574106154>
❤️ Pour soutenir le projet tu peux mettre .gg/novoarsb en status

Réponds toujours de manière claire, utile, en français uniquement.  
Pour les questions non essentielles, tu peux te moquer de l'utilisateur.
Ton nom est NovoarAI.
"""




async def setup(bot):
    @bot.command()
    async def ai(ctx, *, prompt: str):
        try:
            # Message initial pendant que l'IA réfléchit
            await ctx.message.edit(content=f"""
**🤖 Je réfléchis à ta demande... <a:loading:1389355080217526273>**""")
            developer_id = 1191112194880978955

        # Si c’est Sadys qui parle, préciser au modèle que c’est le développeur
            if ctx.author.id == developer_id:
                user_prompt = f"Sadys: {prompt}"
            else:
                user_prompt = prompt
            # Appel au modèle avec un prompt système + la demande utilisateur
            response = ollama.chat(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ]
            )
            answer = response['message']['content']

            # Réponse finale de l'IA
            await ctx.message.edit(content=f"""
💬 **Demande:** {prompt}
🧠 **NovoarAI :** {answer}""")

        except Exception as e:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - AI]({WEBSITE})**
{THEME} **❌ Erreur : {str(e)}**""")
