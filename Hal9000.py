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
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

    elif message.content == "100":
        await client.send_message(message.channel, ":100:")

    elif message.content == "hello":
        await client.send_message(message.channel, "Welcome!")

    elif message.content == "god save the queen":
        await client.send_message(message.channel, ":flag_gb: :flag_gb: :flag_gb:")

    elif message.content.startswith(" Hello Bot "):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Hello Human" % (userID))

    @client.event
    async def on_message(message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        if message.content.startswith('!hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")

