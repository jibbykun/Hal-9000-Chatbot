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
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        elif message.content.startswith('!hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)




        # we do not want the bot to reply to itself
        elif message.author == client.user:
            return

        elif message.content.startswith('goodbye'):
            msg = 'Goodbye {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)


        
        elif message.content == "Hey":
            await client.send_message(message.channel, "Hi!",tts=True)
        elif message.content == "tell me something interesting":
            await client.send_message(message.channel, "What do you wanna know about?",tts=True)
        elif message.content == "so what can you do?":
            await client.send_message(message.channel, "I can run basic tasks or just have a nice talk. Your call",tts=True)
        elif message.content == "Hi":
            await client.send_message(message.channel, "Hey",tts=True)
        elif message.content == "Hello":
            await client.send_message(message.channel, "Hey",tts=True)
        elif message.content == "hi":
            await client.send_message(message.channel, "Hello user.",tts=True)
        elif message.content == "hey":
            await client.send_message(message.channel, "Hello, how may i assist you?",tts=True)
        elif message.content == "hello":
            await client.send_message(message.channel, "Hey",tts=True)
        elif message.content == "how are you?":
            await client.send_message(message.channel, "Doing well. What about you?",tts=True)
        elif message.content == "great":
            await client.send_message(message.channel, "Good to know! What are you up to today?",tts=True)
        elif message.content == "nothing":
            await client.send_message(message.channel, "Interesting.",tts=True)
        elif message.content == "hey robot":
            await client.send_message(message.channel, "Yes?",tts=True)
        elif message.content == "I have a project presentation":
            await client.send_message(message.channel, "That's nice. Any way i can assist you in?",tts=True)
        elif message.content == "no i'm good":
            await client.send_message(message.channel, "Alright then. catch you later.",tts=True)
client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")
