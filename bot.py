import discord
import random
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

# setup
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

# events
@bot.event
async def on_ready():
    print(f'✅ {bot.user.name} is online!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower() == "hello":
        await message.channel.send(f"Hi {message.author.display_name}! 👋")
    
    # This allows the @bot.commands below to work
    await bot.process_commands(message)

# commands
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

@bot.command()
async def roll(ctx):
    result = random.randint(1, 6)
    await ctx.send(f'🎲 You rolled a {result}!')

# run bot
print("Attempting to launch the bot...")
bot.run(TOKEN)