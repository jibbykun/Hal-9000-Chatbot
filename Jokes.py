import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Hello Dave")

@client.event
async def on_message(message):

    if message.content == "Can you tell me a joke?":

        jokes = ["What would you call a spud at a rock concert? A mosh potato!", "Why does Waldo wear a striped shirt? Because he doesn't want to be spotted!", "What's the difference between a cat and a comma? A cat has claws at the end of its paws and a comma is a pause at the end of a clause.", "Where do polar bears keep their money? In a snow bank!", "What did the finger say to the thumb? I'm in glove with you!", "What do a dog and a phone have in common? They both have collar ID."]

        await client.send_message(message.channel, random.choice(jokes))


client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")