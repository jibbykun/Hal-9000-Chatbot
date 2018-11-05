import discord
from discord.ext.commands import bot
from discord.ext import commands
import random

Client = discord.Client()
client = commands.Bot(command_prefix="!")

"""
num1 = input("enter number 1")
num2 = input("enter number 2")
result = 0
choice = input("which operation would you like?")
if choice == "+":
    result = num1 + num2
    print (result)
elif choice == "*":
    result = num1 * num2
    print (result)
"""


@client.event
async def on_ready():
    print("Hello Dave")

@client.event
async def on_message(message):
    mathcheck = message.content
    if "math" in mathcheck:
        await client.send_message(message.channel, "need help with some maths? Ok then, enter your first number")
        firstnumber = message.content
        await client.send_message(message.channel, "ok, now enter a second number")
        secondnumber = message.content
        await client.send_message(message.channel, "which operation do you want? enter either +, -, * or /")
        choice = message.content
        result = 0
        if choice == "+":
            result = firstnumber + secondnumber
            await client.send_message(message.channel, result)
            responses = ("Anything else?", "What else can help you with?", "I hope that was useful", "A good day to be productive!")
            await client.send_message(message.channel, random.choice(responses))






client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")