import discord
from discord.ext import commands
from datetime import datetime
import os

async def setup(bot):  # Chargement dynamique du module

    @bot.command()
    async def heartlog(ctx, *, arg=None):
        log_file = "heartlog.txt"

        if arg is None:
            await ctx.message.edit(content="❗ Utilisation : `heartlog <message>` ou `heartlog list`")
            return

        if arg.lower() == "list":
            if not os.path.exists(log_file):
                await ctx.message.edit(content="📭 Ton cœur est encore silencieux. Aucun message enregistré.")
                return

            with open(log_file, "r", encoding="utf-8") as f:
                entries = f.readlines()

            if not entries:
                await ctx.message.edit(content="📭 Ton cœur est encore silencieux. Aucun message enregistré.")
                return

            MAX_DISPLAY = 10
            display = entries[-MAX_DISPLAY:]
            content = "🖤 Heartlog — Derniers messages :\n" + "".join(display) + f"\n📄 Total : {len(entries)} message(s)."

            await ctx.message.edit(content=content)

        else:
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
            log_entry = f"[{timestamp}] {arg}\n"

            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)

            await ctx.message.edit(content="📝 Ton message a été gravé dans ton cœur numérique.")
