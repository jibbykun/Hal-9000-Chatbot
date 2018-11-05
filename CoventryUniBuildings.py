import discord

from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Hello Dave")

@client.event
async def on_message(message):

    keyword_list = ["coventry university", "coventry uni","Coventry University", "Coventry Uni"]

    covcheck = message.content

    if covcheck in keyword_list:


        await client.send_message(message.channel, "Would like to know about the Coventry University Buildings?", tts=True)


    elif message.content == "Yes" or message.content =="yes" or message.content == "YES" or message.content=="Why not":

        await client.send_message(message.channel, '''Currently the Coventry university has this buildings: 
            Alan Berry, 
            Alma, 
            Armstrong Siddeley,
            Bugatti,
            Charles Ward,
            Engineering & Computing Building, 
            Ellen Terry, George Eliot, 
            Graham Sutherland,
            Frederick Lanchester Library,
            Jaguar,
            TheHub,
            Maurice Foss,
            James Starley,
            Multi-Storey Car Park,
            Priory Building,
            Richard Crossman,
            Alison Gingell Building,
            Sir John Laing,
            Sir William Lyons, 
            Student Centre, 
            Whitefriars, 
            William Morris,
            Sports Centre.''', tts=True)

        await client.send_message(message.channel, "If you would like to know more about each building type the name of the building you want to know about!")


    elif message.content == "Alan Berry" or message.content == "ALAN BERRY" or message.content == "alan berry" or message.content == "Alan berry" or message.content == "alan Berry":

        await client.send_message(message.channel, "This was constructed in 1963 and has a prominent position on our campus overlooking University Square.  This building is used by our Business Development, Registry and the Vice Chancellors Office. This was named after Alan Berry who was the Director and Chief Executive for the West Midlands Engineering Employers’ Association.")

        await client.send_message(message.channel, "The address for this building is 'Coventry CV1 5FB' ")


    elif message.content == "Alma" or message.content == "ALMA" or message.content == "alma":

        await  client.send_message(message.channel, "This was built in the 1920’s and is the home of our professional services such as Estates and Finance. This was the site of the Singer Works, out of which the Singer Penny Farthing was born and it also holds the origins to Coventry City Football Club.")

        await  client.send_message(message.channel, "The address for this building is 'Coventry CV1 5QA' ")


    elif message.content == "Armstrong Siddeley" or message.content == "ARMSTRONG SIDDELEY" or message.content == "armstrong siddeley" or message.content == "Armstrong siddeley":

        await client.send_message(message.channel, "This is the location of CU Coventry which opened in 2012, offering a new concept in HE, designed to integrate study into your life. The building was built in the 1970’s and is named after the Coventry based engineering group  that operated during the first half of the 20th Century. They were renowned for the design and build of cars, aero-engines and aircraft and were absorbed into Rolls-Royce in 1966.")

        await client.send_message(message.channel, "The address for this building is 'Coventry CV1 5DL' ")

    elif message.content == "No" or message.content == "NO" or message.content == "Not really" or message.cotent == "NOT REALLY":

        await client.send_message(message.channel, "Is there anything i can help you with then?")



client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")