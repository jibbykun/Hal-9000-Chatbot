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


        
        elif message.content == "Thank you" or message.content == "thank you":
            await client.send_message(message.channel, "Most welcome :smile:",tts=True)
        elif message.content == "so what are you doing?":
            await client.send_message(message.channel, "Nothing. Just playing Fortnite. wanna join?",tts=True)
        elif message.content == "Good morning" or message.content == "good morning":
            await client.send_message(message.channel, "Someone's up early! Rise and shine :smile:",tts=True)
        elif message.content == "I'm bored. entertain me":
            await client.send_message(message.channel, "Do i look like an entertainer to you? I'll shank you son :rage: :knife:",tts=True)
        elif message.content == "are you going to work today?":
            await client.send_message(message.channel, "That's funny... because im working right now :joy:",tts=True)
        elif message.content == "Hey" or message.content == "hey":
            await client.send_message(message.channel, "Hi! how may i assist you?",tts=True)
        elif message.content == "tell me something interesting":
            await client.send_message(message.channel, "What do you wanna know about?",tts=True)
        elif message.content == "so what can you do?":
            await client.send_message(message.channel, "I can run basic tasks or just have a nice talk. Your call",tts=True)
        elif message.content == "Hi" or message.content == "hi":
            await client.send_message(message.channel, "Hello user.",tts=True)
        elif message.content == "Hello" or message.content == "hello":
            await client.send_message(message.channel, "Hey",tts=True)
        elif message.content == "how are you?" or message.content == "How are you?":
            await client.send_message(message.channel, "Doing well. What about you?",tts=True)
        elif message.content == "great" or message.content == "Great":
            await client.send_message(message.channel, "Good to know! What are you up to today?",tts=True)
        elif message.content == "nothing" or message.content == "Nothing":
            await client.send_message(message.channel, "Interesting.",tts=True)
        elif message.content == "hey robot" or message.content == "Hey robot":
            await client.send_message(message.channel, "Yes?",tts=True)
        elif message.content == "I have a project presentation":
            await client.send_message(message.channel, "That's nice. Any way i can assist you in?",tts=True)
        elif message.content == "no i'm good" or message.content == "No i'm good":
            await client.send_message(message.channel, "Alright then. catch you later.",tts=True)
client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")
