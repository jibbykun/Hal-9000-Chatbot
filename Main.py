import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Hello Dave")


@client.event
async def on_message(message):
    shakespearetriggers = ("HAMLET", "SHAKESPEARE", "ROMEO", "JULIET", "PLAY", "THEATRE")
    message.content = message.content.upper()
    if "WEATHER" in message.content:
        os.system('weather.py')
    elif "HELP" in message.content:
        os.system('help.py')
    elif shakespearetriggers in message.content:
        os.system('Shakespeare.py')
    elif "JOKES" in message.content:
        os.system('jokes.py')
    elif "TIME" in message.content:
        os.system('Time.py')
    else:
        await client.send_message(message.channel, "beep boop")

client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")