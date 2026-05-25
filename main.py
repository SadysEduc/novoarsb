import os
import json
import asyncio
import threading
import discord
from discord.ext import commands
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text

with open('config.json') as f:
    config = json.load(f)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
WEBSITE = config.get('website', 'https://discord.gg/novoarsb')
THEME = config.get('theme', '> -')

console = Console()
bot = commands.Bot(command_prefix=PREFIX, help_command=None, self_bot=True)

loaded_modules = []
failed_modules = {}



async def load_commands(bot):
    directories = ['utility', 'fun', 'moderation', 'raid', 'help', 'pentest', 'settings', "aic", "backup", "sadys"]
    for directory in directories:
        path = f'commands/{directory}'
        if not os.path.exists(path):
            console.print(f"[red]Le dossier {path} n'existe pas.[/red]")
            continue
        files = [f for f in os.listdir(path) if f.endswith('.py') and not f.startswith('_')]
        for filename in files:
            module_name = f'commands.{directory}.{filename[:-3]}'
            try:
                module = __import__(module_name, fromlist=['setup'])
                if hasattr(module, 'setup'):
                    await module.setup(bot)
                    loaded_modules.append(module_name)
                else:
                    console.print(f"[yellow]Le module {module_name} n'a pas de fonction setup[/yellow]")
                    failed_modules[module_name] = "Pas de fonction setup"
            except Exception as e:
                failed_modules[module_name] = str(e)
                console.print(f"[red]Erreur lors du chargement du module {module_name}: {e}[/red]")

def build_config_panel():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    table = Table.grid(padding=(0,1))
    table.add_column(justify="right", style="bold cyan", no_wrap=True)
    table.add_column(justify="left", style="bold white")
    table.add_row("🕒 Heure :", f"[yellow]{now}[/yellow]")
    table.add_row("📛 Nom :", f"[magenta]{NAME}[/magenta]")
    table.add_row("📍 Préfixe :", f"[green]{PREFIX}[/green]")
    table.add_row("💬 Auto-suppression :", f"[red]{DELTIME}s[/red]")
    table.add_row("🌐 Website :", f"[underline blue]{WEBSITE}[/underline blue]")
    table.add_row("🎨 Thème :", f"[bold]{THEME}[/bold]")
    title_text = Text("🔧 Configuration", style="bold cyan")
    return Panel(table, title=title_text, border_style="bright_cyan", width=50)

def build_user_panel(pseudo, friends_count, guild_count):
    table = Table.grid(padding=1)
    table.add_column(justify="right", no_wrap=True, style="bold green")
    table.add_column(justify="left", style="bold white")
    table.add_row("👤 Pseudo :", pseudo)
    table.add_row("🤝 Amis :", str(friends_count))
    table.add_row("🌍 Serveurs :", str(guild_count))
    return Panel(table, title="🖥️ Infos Utilisateur", border_style="green", width=40)

def build_modules_panel():
    col_count = 3
    table = Table(show_header=False, box=None, pad_edge=False, expand=True)
    for _ in range(col_count):
        table.add_column(justify="left", max_width=30, overflow="fold")
    all_modules = [(m, True) for m in loaded_modules] + [(m, False) for m in failed_modules.keys()]
    all_modules.sort(key=lambda x: x[0].lower())
    rows = []
    for i in range(0, len(all_modules), col_count):
        row = []
        for j in range(col_count):
            idx = i + j
            if idx < len(all_modules):
                mod, is_loaded = all_modules[idx]
                text = f"[green]{mod}[/green]" if is_loaded else f"[red]{mod}[/red]"
                row.append(text)
            else:
                row.append("")
        rows.append(row)
    for row in rows:
        table.add_row(*row)
    return Panel(table, title="📄 Modules chargés / échoués", border_style="magenta", width=90)

async def fetch_user_info(bot):
    user = bot.user
    pseudo = f"{user.name}#{user.discriminator}"
    friends_count = len(user.friends) if hasattr(user, 'friends') else "N/A"
    guild_count = len(bot.guilds)
    return pseudo, friends_count, guild_count

async def display_panels():
    await bot.wait_until_ready()
    console.print("🔄 Chargement des modules...\n")
    await load_commands(bot)
    await asyncio.sleep(3)
    console.clear()
    pseudo, friends_count, guild_count = await fetch_user_info(bot)
    config_panel = build_config_panel()
    user_panel = build_user_panel(pseudo, friends_count, guild_count)
    modules_panel = build_modules_panel()
    console.print(Columns([config_panel, user_panel, modules_panel]))


@bot.event
async def on_ready():
    console.print(f"✅ Connecté en tant que {bot.user}\n")
    asyncio.create_task(display_panels())
    if os.path.exists("data/reboot.json"):
        try:
            with open("data/reboot.json", "r") as f:
                data = json.load(f)
            channel = bot.get_channel(data["channel_id"])
            if channel:
                message = await channel.fetch_message(data["message_id"])
                await message.edit(content="**NovoarSB** redémarré avec succès <a:success:1389362166284685516>")
            os.remove("data/reboot.json")
        except Exception as e:
            print(f"❌ Erreur lors de la mise à jour du message de redémarrage : {e}")

@bot.event
async def on_command(ctx):
    if ctx.command.name not in ["leak", "cars"]:
        try:
            await asyncio.sleep(DELTIME)
            await ctx.message.delete()
        except Exception as e:
            console.print(f"[red]Erreur lors de la suppression d'une commande : {e}[/red]")



bot.run(TOKEN)
import os
import json
import asyncio
import threading
import discord
from discord.ext import commands
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text

with open('config.json') as f:
    config = json.load(f)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
WEBSITE = config.get('website', 'https://discord.gg/novoarsb')
THEME = config.get('theme', '> -')

console = Console()
bot = commands.Bot(command_prefix=PREFIX, help_command=None, self_bot=True)

loaded_modules = []
failed_modules = {}



async def load_commands(bot):
    directories = ['utility', 'fun', 'moderation', 'raid', 'help', 'pentest', 'settings', "aic", "backup", "sadys"]
    for directory in directories:
        path = f'commands/{directory}'
        if not os.path.exists(path):
            console.print(f"[red]Le dossier {path} n'existe pas.[/red]")
            continue
        files = [f for f in os.listdir(path) if f.endswith('.py') and not f.startswith('_')]
        for filename in files:
            module_name = f'commands.{directory}.{filename[:-3]}'
            try:
                module = __import__(module_name, fromlist=['setup'])
                if hasattr(module, 'setup'):
                    await module.setup(bot)
                    loaded_modules.append(module_name)
                else:
                    console.print(f"[yellow]Le module {module_name} n'a pas de fonction setup[/yellow]")
                    failed_modules[module_name] = "Pas de fonction setup"
            except Exception as e:
                failed_modules[module_name] = str(e)
                console.print(f"[red]Erreur lors du chargement du module {module_name}: {e}[/red]")

def build_config_panel():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    table = Table.grid(padding=(0,1))
    table.add_column(justify="right", style="bold cyan", no_wrap=True)
    table.add_column(justify="left", style="bold white")
    table.add_row("🕒 Heure :", f"[yellow]{now}[/yellow]")
    table.add_row("📛 Nom :", f"[magenta]{NAME}[/magenta]")
    table.add_row("📍 Préfixe :", f"[green]{PREFIX}[/green]")
    table.add_row("💬 Auto-suppression :", f"[red]{DELTIME}s[/red]")
    table.add_row("🌐 Website :", f"[underline blue]{WEBSITE}[/underline blue]")
    table.add_row("🎨 Thème :", f"[bold]{THEME}[/bold]")
    title_text = Text("🔧 Configuration", style="bold cyan")
    return Panel(table, title=title_text, border_style="bright_cyan", width=50)

def build_user_panel(pseudo, friends_count, guild_count):
    table = Table.grid(padding=1)
    table.add_column(justify="right", no_wrap=True, style="bold green")
    table.add_column(justify="left", style="bold white")
    table.add_row("👤 Pseudo :", pseudo)
    table.add_row("🤝 Amis :", str(friends_count))
    table.add_row("🌍 Serveurs :", str(guild_count))
    return Panel(table, title="🖥️ Infos Utilisateur", border_style="green", width=40)

def build_modules_panel():
    col_count = 3
    table = Table(show_header=False, box=None, pad_edge=False, expand=True)
    for _ in range(col_count):
        table.add_column(justify="left", max_width=30, overflow="fold")
    all_modules = [(m, True) for m in loaded_modules] + [(m, False) for m in failed_modules.keys()]
    all_modules.sort(key=lambda x: x[0].lower())
    rows = []
    for i in range(0, len(all_modules), col_count):
        row = []
        for j in range(col_count):
            idx = i + j
            if idx < len(all_modules):
                mod, is_loaded = all_modules[idx]
                text = f"[green]{mod}[/green]" if is_loaded else f"[red]{mod}[/red]"
                row.append(text)
            else:
                row.append("")
        rows.append(row)
    for row in rows:
        table.add_row(*row)
    return Panel(table, title="📄 Modules chargés / échoués", border_style="magenta", width=90)

async def fetch_user_info(bot):
    user = bot.user
    pseudo = f"{user.name}#{user.discriminator}"
    friends_count = len(user.friends) if hasattr(user, 'friends') else "N/A"
    guild_count = len(bot.guilds)
    return pseudo, friends_count, guild_count

async def display_panels():
    await bot.wait_until_ready()
    console.print("🔄 Chargement des modules...\n")
    await load_commands(bot)
    await asyncio.sleep(3)
    console.clear()
    pseudo, friends_count, guild_count = await fetch_user_info(bot)
    config_panel = build_config_panel()
    user_panel = build_user_panel(pseudo, friends_count, guild_count)
    modules_panel = build_modules_panel()
    console.print(Columns([config_panel, user_panel, modules_panel]))


@bot.event
async def on_ready():
    console.print(f"✅ Connecté en tant que {bot.user}\n")
    asyncio.create_task(display_panels())
    if os.path.exists("data/reboot.json"):
        try:
            with open("data/reboot.json", "r") as f:
                data = json.load(f)
            channel = bot.get_channel(data["channel_id"])
            if channel:
                message = await channel.fetch_message(data["message_id"])
                await message.edit(content="**NovoarSB** redémarré avec succès <a:success:1389362166284685516>")
            os.remove("data/reboot.json")
        except Exception as e:
            print(f"❌ Erreur lors de la mise à jour du message de redémarrage : {e}")

@bot.event
async def on_command(ctx):
    if ctx.command.name not in ["leak", "cars"]:
        try:
            await asyncio.sleep(DELTIME)
            await ctx.message.delete()
        except Exception as e:
            console.print(f"[red]Erreur lors de la suppression d'une commande : {e}[/red]")



bot.run(TOKEN)
