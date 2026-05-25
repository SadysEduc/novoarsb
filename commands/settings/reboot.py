import os
import sys
import json
from discord.ext import commands




async def setup(bot):
    @bot.command(name="reboot")
    async def reboot(ctx: commands.Context):
        try:
            msg = await ctx.message.edit(content="Redémarrage de **NovoarSB**... <a:loading:1389355080217526273>")

            # Créer le dossier 'data' s'il n'existe pas
            os.makedirs("data", exist_ok=True)

            # Sauvegarder l'ID du message et du channel
            with open("data/reboot.json", "w") as f:
                json.dump({
                    "channel_id": ctx.channel.id,
                    "message_id": msg.id
                }, f)

            # ⚠️ Pas de await bot.close()
            # Reboot immédiat du script
            os.execl(sys.executable, sys.executable, *sys.argv)

        except Exception as e:
            await ctx.send(f"❌ Erreur lors du redémarrage : `{e}`")
