import discord

from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Hello Dave")

@client.event
async def on_message(message):

    message.content = message.content.upper()

    if message.content == "!HELP":

        commands = ("If you type coventry university or coventry uni a script about the coventry university buildings will run!", "If you type can you tell me a joke? a script that tells jokes will run!")

        await client.send_message(message.channel, "Here is a list of commands: ")

        for command in commands:
            await client.send_message(message.channel, command)




client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")