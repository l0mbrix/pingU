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

bot.run(TOKEN)