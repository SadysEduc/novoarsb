import json
import aiohttp
from bs4 import BeautifulSoup
import discord
from discord.ext import commands


with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
GENIUS_TOKEN = config['genius_token']
THEME = config['theme']
WEBSITE = config['website']

async def setup(bot):
    @bot.command()
    async def lyrics(ctx, *, song_title: str):
        try:
            await ctx.message.edit(content=f"{THEME} Recherche des paroles pour **{song_title}**...")

            headers = {"Authorization": f"Bearer {GENIUS_TOKEN}"}
            search_url = f"https://api.genius.com/search?q={song_title}"

            async with aiohttp.ClientSession() as session:
                async with session.get(search_url, headers=headers) as resp:
                    data = await resp.json()
                    hits = data["response"]["hits"]

                    if not hits:
                        await ctx.message.edit(content=f"{THEME} ❌ Aucun résultat trouvé pour **{song_title}**.")
                        return

                    song_url = hits[0]["result"]["url"]

                async with session.get(song_url) as song_page:
                    html = await song_page.text()
                    soup = BeautifulSoup(html, "html.parser")

                    
                    lyrics_blocks = soup.select("div[class^='Lyrics__Container'], div.lyrics")

                    if not lyrics_blocks:
                        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Lyrics]({WEBSITE})**
{THEME} ❌ Paroles introuvables pour **{song_title}**.""")
                        return

                    lyrics = "\n\n".join([block.get_text(separator="\n").strip() for block in lyrics_blocks])
                    lyrics = lyrics.strip()

                    if not lyrics:
                        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Lyrics]({WEBSITE})**
{THEME} ❌ Aucune parole détectée pour **{song_title}**.""")
                        return

                    if len(lyrics) > 1900:
                        lyrics = lyrics[:1900] + "\n[...]"

                    await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Lyrics]({WEBSITE})**
{THEME} Paroles pour **{song_title}** :
```{lyrics}```""")

        except Exception as e:
            await ctx.message.edit(content=f"{THEME} ❌ Erreur : `{e}`")
