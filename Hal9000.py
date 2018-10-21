import discord
from discord.ext.commands import bot
from discord.ext import commands
import asysncio
import time

Client = discord.Client ()
client = commands.Bot (command_prefix = "!")

@client.event
async def on_ready():
    print ("Hello Dave")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")
