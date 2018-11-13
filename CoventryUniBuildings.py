import discord

from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Hello Dave")

last_message = ""

@client.event
async def on_message(message):

    global last_message

    message.content = message.content.upper()

    agreement_list = ["YES", "SURE", "WHY NOT"]

    keyword_list = ["COVENTRY UNIVERSITY", "COVENTRY UNI"]

    buildings_list = ["ALAN BERRY", "ALMA", "ARMSTRONG SIDDELEY", "BUGATTI", "CHARLES WARD", "ENGINNERING & COMPUTING BUILDING", "ELLEN TERRY", "GEORGE ELLIOT","GRAHAM SUTHERLAND","FREDERICK LANCHESTER LIBRARY", "JAGUAR", "THEHUB", "MAURICE FOSS", "JAMES STARLEY","MULTI-STOREY CAR PARK", "PRIORY BUILDING", "RICHARD CROSSMAN", "ALISON GINGELL BUILDING", "SIR JOHN LAING", "SIR WILLIAM LYONS", "STUDENT CENTRE", "WHITEFRIARS", "WILLIAM MORRIS", "SPORTS CENTRE"]

    if message.content in keyword_list:

        await client.send_message(message.channel, "Would you like to know about the Coventry University Buildings?")

    elif message.content in agreement_list:
        last_message = message.content
        await client.send_message(message.channel, "Currently the coventry university has this buildings: ")

        for building in buildings_list:
            await client.send_message(message.channel, building)

        await client.send_message(message.channel, "If you would like to know more about each building type the name of the building you want to know about!")
        last_message = ""

    elif not(last_message in agreement_list) and message.content == buildings_list[0]:

        await client.send_message(message.channel, "This was constructed in 1963 and has a prominent position on our campus overlooking University Square.  This building is used by our Business Development, Registry and the Vice Chancellors Office. This was named after Alan Berry who was the Director and Chief Executive for the West Midlands Engineering Employers’ Association.")

        await client.send_message(message.channel, "The address for this building is 'Coventry CV1 5FB' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[1]:

        await  client.send_message(message.channel, "This was built in the 1920’s and is the home of our professional services such as Estates and Finance. This was the site of the Singer Works, out of which the Singer Penny Farthing was born and it also holds the origins to Coventry City Football Club.")

        await  client.send_message(message.channel, "The address for this building is 'Alma St, Coventry CV1 5QA' ")

    elif  not(last_message in agreement_list) and message.content == buildings_list[2]:

        await client.send_message(message.channel, "This is the location of CU Coventry which opened in 2012, offering a new concept in HE, designed to integrate study into your life. The building was built in the 1970’s and is named after the Coventry based engineering group  that operated during the first half of the 20th Century. They were renowned for the design and build of cars, aero-engines and aircraft and were absorbed into Rolls-Royce in 1966.")

        await client.send_message(message.channel, "The address for this building is 'Coventry CV1 5DL' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[3]:

        await  client.send_message(message.channel, "This building funded by the Bugatti trust was built in 2002 and provides a valuable space for our Faculty of Arts and Humanities. In particular this is used in the areas of Automotive & Transport Design with very strong industry links.")

        await  client.send_message(message.channel, "The address for this building is 'Grove St, Coventry CV1 5PH' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[4]:

        await  client.send_message(message.channel, "Built in the 1950’s this building is used mainly by our Faculty of Health and Life Sciences. The building was named after a key figure for the University, who was a University Governor, and became Vice Chair of the Board of Governors in 1982.")

        await  client.send_message(message.channel, "The address for this building is 'Coventry University, Cope St, Coventry CV1 5FD'")

    elif not(last_message in agreement_list) and message.content == buildings_list[5]:

        await  client.send_message(message.channel, "This building was completed in 2012 and is used solely by our Faculty of Engineering, Environment and Computing. The £50m project delivered a highly sustainable building that uses a range of technologies including rainwater harvesting, solar thermal energy and biomass boilers. Facilities include a high precision wind-tunnel, a £3m high-performance engineering centre, a Harrier Jump Jet, three flight simulators and the UK’s largest magnet.")

        await  client.send_message(message.channel, "The address for this building is '1 Gulson Rd, Coventry CV1 2JH' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[6]:

        await  client.send_message(message.channel, "This building is used by our Faculty of Arts and Humanities, specifically for the Performing Arts, Media and Music Students. Fittingly this building previously was a cinema, originally built in 1880 with a major refurbishment in 2000. The building has been named after Dame Ellen Terry, a star of the Victoria stage and a leading Shakespearean actress.")

        await  client.send_message(message.channel, "The address for this building is '34-35 Jordan Well, Coventry CV1 5RW")

    elif not(last_message in agreement_list) and message.content == buildings_list[7]:

        await  client.send_message(message.channel, "This building was built in 1960 and is used solely by our Faculty of Business and Law. George Eliot is the pen name of the novelist Mary Anne Evans (1819-1880) and was one of the leading writers of the Victorian era.")

        await  client.send_message(message.channel, "The address for this building is 'Priory St, Coventry CV1 5FB' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[8]:

        await client.send_message(message.channel, "Built in 1959, this building is used by our Faculty of Arts and Humanities, predominately for the Design and Visual Art students, fitted with a full commercial fashion studio. This building was aptly named after the painter and print maker who created the world famous tapestry Christ in Glory hanging in Coventry Cathedral.")

        await client.send_message(message.channel, "The address for this building is 'Cox St, Coventry CV1 5PH' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[9]:

        await client.send_message(message.channel, "This modern and striking building houses the main University library, and was completed in 2001. It has been named after the Coventry based designer of the first British petrol-driven car. With a number of different study zones across 5 floors, it provides an invaluable central study and resource space for staff and students. It is equipped with over 350 computers, group and individual study rooms, books, journals, and electronic resources.")

        await client.send_message(message.channel, "The address for this building is 'Frederick Lanchester Building, Coventry University, Gosford St, Coventry CV1 5DD' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[10]:

        await client.send_message(message.channel, "This building was built in the late 1970’s and sponsored by the Coventry based car manufacturer. It has recently undergone a significant refurbishment, with additional improvements planned.  It is now home to our Postgraduate students, as well as our researchers within the Centre for Business in Society (CBiS). ")

        await client.send_message(message.channel, "The address for this building is 'Coventry University, 113A Gosford St, Coventry CV1 5DL' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[11]:

        await client.send_message(message.channel, "Completed in 2011 TheHub is a modern, hi-tech building providing a welcoming social space for our students. Facilities in the building include a doctors’ surgery, a multi-cultural faith centre, employment services, catering services, as well as hairdressers, food court and the Students’ Union offices. This building also has a large fully licensed function space with bars and a multi-purpose venue space. The building achieved a BREEAM status of Excellent.")

        await client.send_message(message.channel, "The address for this building is 'Priory St, Coventry CV1 5FB' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[12]:

        await client.send_message(message.channel, "Built in 1978, this building is used by our Faculty of Arts and Humanities, who mainly run their Industrial Design courses from here. The building has been named after the former Deputy Director of Coventry Polytechnic and one of the University’s Honorary Life Fellows.")

        await client.send_message(message.channel, "The address for this building is 'Cox St, Coventry CV1 5PH' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[13]:

        await client.send_message(message.channel, "Built in the late 1950’s, this is home to our Faculty of Health and Life Sciences. It was named after the British inventor of the Coventry tricycle and father of the bicycle industry.")

        await client.send_message(message.channel, "The address for this building is '213 Cox St, Coventry CV1 5PH' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[14]:

        await client.send_message(message.channel, "This is our impressive Multi-storey car park, opened for staff and visitors in 2010. It has 457 spaces over 15 floors, including spaces for electric vehicles.")

        await client.send_message(message.channel, "The address for this building is '65-66 Gosford St, Coventry CV1 5DL' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[15]:

        await client.send_message(message.channel, "Built in 1964, this building is occupied by the Cambridge Education Group, who run their Foundation Campus from here. They offer University Pathway courses for foreign students who wish to gain entry to UK Universities. Also in this building is a large sports hall, and the University’s Student Union Radio.")

        await client.send_message(message.channel, "The address for this building is 'Priory Building, Coventry CV1 5FJ' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[16]:

        await client.send_message(message.channel, "This was built in 1971 and has been named after the political journalist and Labour politician, representing Coventry East from 1945-1974. This is the main building for the Faculty of Health and Life Sciences and includes a mock hospital ward and operating theatre, complete with sink scrubs and theatre lights.")

        await client.send_message(message.channel, "The address for this building is 'Jordan Well, Coventry CV1 5RW' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[17]:

        await client.send_message(message.channel, "Built in 2017, the new facility was opened by the Duke and Duchess of Cambridge in January 2018. The £59m building allows students to learn to care for a patient at every stage of their healthcare experience.")

        await client.send_message(message.channel, "The address for this building is 'Coventry CV1 5FB' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[18]:

        await client.send_message(message.channel, "This building was built in 1970, and was named after the knighted British entrepreneur in the construction industry. This building is primarily used by the Faculty of Engineering, Environment and Computing, offering courses relating to the construction industry.")

        await client.send_message(message.channel, "The address for this building is 'Much Park St, Coventry CV1 2LT' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[19]:

        await client.send_message(message.channel, "Constructed in1980, this building is home to our IT services. Sir William Lyons was the co-founder of the Swallow Sidecar Company which subsequently became Jaguar Cars Limited.")

        await client.send_message(message.channel, "The address for this building is 'Gosford St, Coventry CV1 5DL' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[20]:

        await client.send_message(message.channel, "Construction was completed in 2006, and as its name suggests is home to some key student services as well as our International Office. This is where our students enroll as well as the main information point for student accommodation and finance queries.")

        await client.send_message(message.channel, "The address for this building is '1 Gulson Rd, Coventry CV1 2JH' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[21]:

        await client.send_message(message.channel, "This is a small office used by our Faculty of Health and Life Sciences. Built in 1922 and its name is drawn from the Carmelite Friary founded in 1342 in Coventry.")

        await client.send_message(message.channel, "The address for this building is '62 Whitefriars St, Coventry CV1 2DS' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[22]:

        await client.send_message(message.channel, "This building began life in 1910 as a factory and has been named after the founder of the Morris car company who used this building as part of its engine production unit. It was converted for use by the University and is now occupied by our Faculty of Business and Law. ")

        await client.send_message(message.channel, "The address for this building is 'Gosford St, Coventry CV1 5DL' ")

    elif not(last_message in agreement_list) and message.content == buildings_list[23]:

        await client.send_message(message.channel, "Our own Sports and Recreation Centre offers a wide range of activities for all sporting tastes, available for use by Staff and Students. Most of the University accommodation includes free membership to the Centre.")

        await client.send_message(message.channel, "The address for this building is 'Whitefriars Ln, Coventry CV1 2DS' ")

    elif message.content == "NO":

        await client.send_message(message.channel, "Is there anything i can help you with then?")
        last_message = message.content



client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")