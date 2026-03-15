import os
from discord.ext import commands

async def setup(bot):

    @bot.command()
    async def heartburn(ctx):
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        if not os.path.exists("heartlog.txt"):
            await ctx.message.edit(content="📭 Ton cœur est déjà vide. Mais le vide, lui, parle fort.")
            return

        await ctx.message.edit(content=(
            "❗ Es-tu sûr de vouloir effacer ton cœur numérique ?\n"
            "_Cela ne changera rien... Les souvenirs resteront gravés en toi._\n"
            "Peut-être... vaut-il mieux garder les traces, comme preuve que tu as aimé ?\n\n"
            "**Tape `oui` pour confirmer, `non` pour annuler.**"
        ))

        try:
            msg = await bot.wait_for("message", timeout=30.0, check=check)
            if msg.content.lower() == "oui":
                os.remove("heartlog.txt")
                await ctx.message.edit(content=(
                    "🔥 Les mots ont disparu... mais le poids reste.\n"
                    "_Tu as effacé l'écriture, pas l'histoire._"
                ))
            else:
                await ctx.message.edit(content="❌ Tu as choisi de garder les cicatrices. Et parfois… c’est ce qu’il faut.")
        except:
            await ctx.message.edit(content="⌛ Temps écoulé. Ton cœur reste intact… pour l’instant.")
