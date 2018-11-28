import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import random
from speech import *

Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Hello Dave")


@client.event


CONVERSING = True

memory = []
greetings = ['hola', 'hello', 'hi', 'hey!', 'Hello', 'Hi']
questions = ['How are you?', 'How are you doing?']
responses = ['Okay', 'I am fine']
validations = ['yes', 'yeah', 'yea', 'no', 'No', 'Nah', 'nah']
verifications = ['Are you sure?', 'You sure?', 'you sure?', 'sure?', "Sure?"]

while CONVERSING:
    lang = 'en-US'
    speed = .3

    if userInput in greetings:
        random_greeting = random.choice(greetings)
        say(random_greeting, lang, speed)
        print(random_greeting)
        memory.append((userInput, random_greeting))
    elif userInput in questions:
        random_response = random.choice(responses)
        say(random_response, lang, speed)
        memory.append((userInput, random_response))
        print(random_response)
    elif userInput in verifications:
        random_response = random.choice(validations)
        say(random_response, lang, speed)
        memory.append((userInput, random_response))
        print(random_response)
    elif 'sure' in userInput:
        response = "Sure about what?"
        say(response, lang, speed)
        memory.append(('sure', response))
        print(response)
    else:
        say("I did not understand what you said. Goodbye", lang, speed)
        CONVERSING = False

for conversations in memory:
    print(conversations)

'''This can be extended with elif statements and eventually you will eventually have your very own slightly clever AI. Just make sure that the else statement is always at the bottom of your code'''

client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")
