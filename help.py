import discord
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Help script ready")

@client.event
async def on_message(message):

    message.content = message.content.upper()

    if message.content == "!HELP":

        commands = ("If you mention coventry university or coventry uni I can give you information about the coventry university buildings!", "If you mention joke I can tell you a joke!", "If you mention the words HAMLET, SHAKESPEARE, ROMEO, JULIET, PLAY, THEATRE, I can show you a shakespearean insult!", "If you mention the time I can give you updated time and date information!", "If you mention the weather I can give you the weather forecast of Coventry!" )

        await client.send_message(message.channel, "Here is a list of commands: ")

        for command in commands:
            await client.send_message(message.channel, command)

client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")
