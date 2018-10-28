import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
from weather import Weather, Unit

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Hello Dave")

@client.event
async def on_message(message):
    if message.content == "Birmingham":
        weather = Weather(unit=Unit.CELSIUS)
        location = weather.lookup_by_location('Birmingham')

        forecasts = location.forecast
        for forecast in forecasts:
            await client.send_message(message.channel, "Forecast: " + forecast.text + " Date: " + forecast.date )
            await client.send_message(message.channel, "High: " + forecast.high + " Low: " + forecast.low)
            await client.send_message(message.channel, "Day: " + forecast.day)



client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")