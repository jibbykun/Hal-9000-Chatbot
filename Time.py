import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix="!")


currentDT = datetime.datetime.now()

@client.event
async def on_message(message):
    timecheck=message.content
    if "time" in timecheck:
        await client.send_message(message.channel, currentDT)

client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")
