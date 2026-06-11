import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("PingU is ready!")
    await bot.tree.sync()
    print("Command synchronized!")

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