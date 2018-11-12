import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Hello Dave")


@client.event
async def on_message(message):
    if message.content == "Hey" or message.content == "Hello":
            await client.send_message(message.channel, "Hi! How can I help you?",tts=True)
    elif message.content == "Can you tell me the event prices?" or message.content == "can you tell me the event prices?":
            await client.send_message(message.channel, "Sure! which event are you looking for?",tts=True)
    elif message.content == "Kasbah" or message.content == "kasbah":
            await client.send_message(message.channel, "Tonight Kasbah has no special event but the entry fee is for 8 pounds!",tts=True)
    elif message.content == "Can you send me the link?" or message.content == "can you send me the link?":
            await client.send_message(message.channel, "Here's the link to kasbah.. https://www.kasbahnightclub.com/",tts=True)
    elif message.content == "empire" or message.content == "Empire":
            await client.send_message(message.channel, "Empire has a number of events throughout the month of November. Do you wanna check it out?",tts=True)
    elif message.content == "Yes" or message.content == "sure":
            await client.send_message(message.channel, "Let me redirect you: http://www.coventryempire.co.uk/ ",tts=True)
client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")
