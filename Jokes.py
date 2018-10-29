import discord

from discord.ext import commands

import random

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Hello Dave")

@client.event
async def on_message(message):

    if message.content == "Can you tell me a joke?":

        jokes = ["What would you call a spud at a rock concert? A mosh potato!","Why does Waldo wear a striped shirt? Because he doesn't want to be spotted!", "What's the difference between a cat and a comma? A cat has claws at the end of its paws and a comma is a pause at the end of a clause.","Where do polar bears keep their money? In a snow bank!","What did the finger say to the thumb? I'm in glove with you!","What do a dog and a phone have in common? They both have collar ID.","What’s brown and sticky? Wait for it... a stick!", "I wondered why the baseball was getting bigger… the it hit me.","What did the dog say after a long day of work? Today was ruff.", "What kind of shoes do ninjas wear? Sneakers", "Why did the Banker quit his job? He lost his interest!", "How does NASA organize a party? They planet", "Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.", "Why can't your nose be 12 inches long? Because then it'd be a foot.", "Knock, knock! Who’s there? Abe. Abe who? Abe CDEFJH...", " Why did the PowerPoint Presentation cross the road? To get to the other slide.", "I used to dislike the idea of having a beard. But then it grew on me"]

        await client.send_message(message.channel, random.choice(jokes))


client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")