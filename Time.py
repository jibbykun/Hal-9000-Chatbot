import discord
from discord.ext import commands
import datetime  #built in datetime function used for this script
import random #for the responses

Client = discord.Client()
client = commands.Bot(command_prefix="!")


currentDT = datetime.datetime.now()

@client.event
async def on_message(message):
    timecheck = message.content
    if "time" in timecheck:
        await client.send_message(message.channel, currentDT)
        responses = ("Anything else?", "What else can help you with?", "I hope that was useful", "A good day to be productive!")
        await client.send_message(message.channel, random.choice(responses))



client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")
