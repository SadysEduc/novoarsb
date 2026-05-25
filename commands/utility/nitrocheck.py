import json
import discord
import requests as r
from discord.ext import commands

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
    async def nitrocheck(ctx, code: str):
        try:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Nitro Check]({WEBSITE})**
{THEME} **Code Nitro :** Vérification en cours...""")

            # Nettoyer le code si c'est un lien complet
            if "discord.gift/" in code:
                code = code.split("discord.gift/")[1]

            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
            headers = {
                "Authorization": TOKEN,  # Optionnel, utile si besoin d'auth
                "User-Agent": "Mozilla/5.0"
            }

            res = r.get(url, headers=headers)
            if res.status_code == 200:
                data = res.json()
                redeemed = data.get("redeemed", False)
                sku_name = data.get("subscription_plan", {}).get("name", "Inconnu")
                gift_type = data.get("type", "Inconnu")

                status = "✅ Valide" if not redeemed else "❌ Déjà utilisé"
                await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Nitro Check]({WEBSITE})**
{THEME} **Code Nitro :** `{code}`
{THEME} **Statut :** {status}
{THEME} **Type d'abonnement :** {sku_name}
{THEME} **Type de cadeau :** {gift_type}
""")
            elif res.status_code == 404:
                await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Nitro Check]({WEBSITE})**
{THEME} ❌ Code Nitro invalide ou inexistant.""")
            else:
                await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Nitro Check]({WEBSITE})**
{THEME} ⚠️ Erreur inconnue lors de la vérification (status {res.status_code}).""")

        except Exception as e:
            await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Nitro Check]({WEBSITE})**
{THEME} **Erreur :** `{e}`""")
