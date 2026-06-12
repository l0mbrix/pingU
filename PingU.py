import os
import discord
import random
import datetime

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
event = datetime.date(2026, 8, 13)

@bot.event
async def on_ready():
    print("PingU is ready!")
    await bot.tree.sync()
    print("Command synchronized!")

@bot.tree.command(name="hhbfest", description="Compte les dodos avant le HHB Fest")
async def hhbfest(interaction: discord.Interaction):
    gif_list = [
        "https://tenor.com/view/oooh-chris-pratt-parks-and-rec-surprised-shocked-gif-14609379",
        "https://tenor.com/view/wiggle-shaquille-o-neal-shake-gif-13935192",
        "https://tenor.com/view/spongebob-squidward-krabby-patty-smug-spongebob-squarepants-gif-9547716225990610286",
        "https://tenor.com/view/toddlers-and-tiaras-big-grin-excited-girl-giddy-smile-gif-9689369815152198607",
        "https://tenor.com/view/dancing-dance-happy-dance-carlton-the-carlton-gif-5314808"
    ]
    gif_chosen = random.choice(gif_list)
    today = datetime.date.today()
    difference = (event - today).days
    days = difference if difference >= 0 else 0
    await interaction.response.send_message(f"Plus que {days} dodos avant le HHB Fest ! {gif_chosen}")

@bot.tree.command(name="pingvalo", description="Ping les joueurs de Valorant")
async def pingvalo(interaction: discord.Interaction):
    gif_list = [
        "https://tenor.com/view/anchorman-team-assemble-team-assemble-gif-20674250",
        "https://tenor.com/view/click-gif-24475537",
        "https://tenor.com/view/ben-stiller-dodgeball-gif-25279767"
    ]
    gif_chosen = random.choice(gif_list)
    await interaction.response.send_message(f"<@&1514279036313014343> {gif_chosen}")

@bot.tree.command(name="pingdemo", description="Ping les joueurs de la Démocratie")
async def pingdemo(interaction:discord.Interaction):
    gif_list = [
        "https://tenor.com/view/helldivers2-helldivers-helldivers-parade-parade-marching-gif-12908433911826180403",
        "https://tenor.com/view/helldiver-helldivers-helldivers-2-frogglish-gif-15658876242661211060",
        "https://tenor.com/view/helldivers-freedom-democracy-spread-gif-7274461004019253594",
        "https://tenor.com/view/helldivers-helldivers-2-super-earth-lets-goo-lets-go-gif-gif-13549931536192156596"
    ]
    gif_chosen = random.choice(gif_list)
    await interaction.response.send_message(f"<@&1514622597042671686> {gif_chosen}")

bot.run(TOKEN)