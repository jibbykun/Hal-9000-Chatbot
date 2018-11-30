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

    agreement_list = ["YES", "SURE", "WHY NOT"]

    keyword_list = ["COVENTRY UNIVERSITY", "COVENTRY UNI"]

    buildings_list = ["1)ALAN BERRY", "2)ALMA", "3)ARMSTRONG SIDDELEY", "4)BUGATTI", "5)CHARLES WARD", "6)ENGINEERING & COMPUTING BUILDING", "7)ELLEN TERRY", "8)GEORGE ELLIOT","9)GRAHAM SUTHERLAND","10)FREDERICK LANCHESTER LIBRARY", "11)JAGUAR", "12)THEHUB", "13)MAURICE FOSS", "14)JAMES STARLEY","15)MULTI-STOREY CAR PARK", "16)PRIORY BUILDING", "17)RICHARD CROSSMAN", "18)ALISON GINGELL BUILDING", "19)SIR JOHN LAING", "20)SIR WILLIAM LYONS", "21)STUDENT CENTRE", "22)WHITEFRIARS", "23)WILLIAM MORRIS", "24)SPORTS CENTRE"]

    if message.content in keyword_list:

        await client.send_message(message.channel, "Would you like to know about the Coventry University Buildings?")

    elif message.content in agreement_list:

        await client.send_message(message.channel, "Currently the coventry university has this buildings: ")

        for building in buildings_list:
            await client.send_message(message.channel, building)

    #Used a for loop to display the buildings in the list because i couldn't do it with (*buildings_list, sep = "\n")

        await client.send_message(message.channel, "If you would like to know more about each building type a number from 1 to 24 and learn more about the building you want to!")


    elif message.content == "1":

        await client.send_message(message.channel, "This was constructed in 1963 and has a prominent position on our campus overlooking University Square.  This building is used by our Business Development, Registry and the Vice Chancellors Office. This was named after Alan Berry who was the Director and Chief Executive for the West Midlands Engineering Employers’ Association.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Alan+Berry,+Coventry+CV1+5FB/@52.4079797,-1.5077411,17z/data=!3m1!4b1!4m5!3m4!1s0x48774bb9795e991b:0x18e7af812a47ced4!8m2!3d52.4079797!4d-1.5055524")

    elif message.content == "2":

        await  client.send_message(message.channel, "This was built in the 1920’s and is the home of our professional services such as Estates and Finance. This was the site of the Singer Works, out of which the Singer Penny Farthing was born and it also holds the origins to Coventry City Football Club.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Alma+Building,+Coventry+University/@52.4100173,-1.5004429,15z/data=!4m2!3m1!1s0x0:0x585688e034ce0d42?ved=2ahUKEwiexqjukOPeAhUHUhoKHbajAB8Q_BIwC3oECAQQCA")

    elif message.content == "3":

        await client.send_message(message.channel, "This is the location of CU Coventry which opened in 2012, offering a new concept in HE, designed to integrate study into your life. The building was built in the 1970’s and is named after the Coventry based engineering group  that operated during the first half of the 20th Century. They were renowned for the design and build of cars, aero-engines and aircraft and were absorbed into Rolls-Royce in 1966.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/CU+Coventry/@52.407583,-1.501042,15z/data=!4m2!3m1!1s0x0:0xa3c20e5f0fae5c64?ved=2ahUKEwjNkq7T4PTeAhVsJMAKHVzQArgQ_BIwDnoECAUQCA")

    elif message.content == "4":

        await  client.send_message(message.channel, "This building funded by the Bugatti trust was built in 2002 and provides a valuable space for our Faculty of Arts and Humanities. In particular this is used in the areas of Automotive & Transport Design with very strong industry links.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Bugatti+Building,+Coventry+University/@52.4078617,-1.5031135,15z/data=!4m2!3m1!1s0x0:0x4c97c71394cf33d7?ved=2ahUKEwjZye354fTeAhXOzaQKHemUDpwQ_BIwDnoECAQQCA")

    elif message.content == "5":

        await  client.send_message(message.channel, "Built in the 1950’s this building is used mainly by our Faculty of Health and Life Sciences. The building was named after a key figure for the University, who was a University Governor, and became Vice Chair of the Board of Governors in 1982.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Charles+Ward+Building,+Coventry+University/@52.408542,-1.505167,15z/data=!4m2!3m1!1s0x0:0xecd8d152bf8934cf?ved=2ahUKEwi6jcKx4vTeAhWEsqQKHbV1DhkQ_BIwDnoECAYQCA")

    elif message.content == "6":

        await  client.send_message(message.channel, "This building was completed in 2012 and is used solely by our Faculty of Engineering, Environment and Computing. The £50m project delivered a highly sustainable building that uses a range of technologies including rainwater harvesting, solar thermal energy and biomass boilers. Facilities include a high precision wind-tunnel, a £3m high-performance engineering centre, a Harrier Jump Jet, three flight simulators and the UK’s largest magnet.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Engineering,+Environment,+%26+Computing+Building,+Coventry+University/@52.4052898,-1.4996593,15z/data=!4m2!3m1!1s0x0:0x65f826135d301789?ved=2ahUKEwihyJXWiePeAhVCxIUKHYlFBPQQ_BIwC3oECAUQCA")

    elif message.content == "7":

        await  client.send_message(message.channel, "This building is used by our Faculty of Arts and Humanities, specifically for the Performing Arts, Media and Music Students. Fittingly this building previously was a cinema, originally built in 1880 with a major refurbishment in 2000. The building has been named after Dame Ellen Terry, a star of the Victoria stage and a leading Shakespearean actress.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Ellen+Terry+Building,+Coventry+University/@52.4066632,-1.5046563,15z/data=!4m2!3m1!1s0x0:0xa2737fe044f57931?ved=2ahUKEwjlsMiwiuPeAhVvyoUKHRL5CagQ_BIwDnoECAEQCA")


    elif message.content == "8":

        await  client.send_message(message.channel, "This building was built in 1960 and is used solely by our Faculty of Business and Law. George Eliot is the pen name of the novelist Mary Anne Evans (1819-1880) and was one of the leading writers of the Victorian era.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.pt/maps/place/George+Eliot+Building,+Coventry+University/@52.4079898,-1.5047571,15z/data=!4m2!3m1!1s0x0:0xb3f18530d23b557b?ved=2ahUKEwjb6bvIiuPeAhVMz4UKHaNHCmMQ_BIwDnoECAYQCA")

    elif message.content == "9":

        await client.send_message(message.channel, "Built in 1959, this building is used by our Faculty of Arts and Humanities, predominately for the Design and Visual Art students, fitted with a full commercial fashion studio. This building was aptly named after the painter and print maker who created the world famous tapestry Christ in Glory hanging in Coventry Cathedral.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Graham+Sutherland+Building,+Coventry+University/@52.4070156,-1.5028692,15z/data=!4m2!3m1!1s0x0:0x2b93803c368fa938?ved=2ahUKEwiL3OiC5PTeAhVIKBoKHcLWCrYQ_BIwDnoECAUQCA")

    elif message.content == "10":

        await client.send_message(message.channel, "This modern and striking building houses the main University library, and was completed in 2001. It has been named after the Coventry based designer of the first British petrol-driven car. With a number of different study zones across 5 floors, it provides an invaluable central study and resource space for staff and students. It is equipped with over 350 computers, group and individual study rooms, books, journals, and electronic resources.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Lanchester+Library/@52.4059622,-1.5005467,15z/data=!4m2!3m1!1s0x0:0x784ad48e50ea81a0?ved=2ahUKEwihvpy05PTeAhVG66QKHYUGCxUQ_BIwDXoECAYQCA")

    elif message.content == "11":

        await client.send_message(message.channel, "This building was built in the late 1970’s and sponsored by the Coventry based car manufacturer. It has recently undergone a significant refurbishment, with additional improvements planned.  It is now home to our Postgraduate students, as well as our researchers within the Centre for Business in Society (CBiS). ")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Jaguar+Building,+Coventry+University/@52.4070482,-1.5010405,15z/data=!4m2!3m1!1s0x0:0x1a329060b746ea63?ved=2ahUKEwiov4Hc3freAhWDGuwKHaD7C0QQ_BIwDnoECAUQCA")

    elif message.content == "12":

        await client.send_message(message.channel, "Completed in 2011 TheHub is a modern, hi-tech building providing a welcoming social space for our students. Facilities in the building include a doctors’ surgery, a multi-cultural faith centre, employment services, catering services, as well as hairdressers, food court and the Students’ Union offices. This building also has a large fully licensed function space with bars and a multi-purpose venue space. The building achieved a BREEAM status of Excellent.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/TheHub,+Coventry+University/@52.4074963,-1.5047307,15z/data=!4m2!3m1!1s0x0:0x83beabca8c39bae0?ved=2ahUKEwjkmaDz3freAhVIzaQKHWGNDpAQ_BIwCnoECAYQCA")

    elif message.content == "13":

        await client.send_message(message.channel, "Built in 1978, this building is used by our Faculty of Arts and Humanities, who mainly run their Industrial Design courses from here. The building has been named after the former Deputy Director of Coventry Polytechnic and one of the University’s Honorary Life Fellows.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Maurice+Foss+Building,+Coventry+University/@52.4078156,-1.5031266,15z/data=!4m2!3m1!1s0x0:0xc6f29bbf224f51b0?ved=2ahUKEwiQkpSN3vreAhUR3KQKHbhBCyoQ_BIwDnoECAUQCA")

    elif message.content == "14":

        await client.send_message(message.channel, "Built in the late 1950’s, this is home to our Faculty of Health and Life Sciences. It was named after the British inventor of the Coventry tricycle and father of the bicycle industry.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/James+Starley+Building,+Coventry+University/@52.4077121,-1.5040618,15z/data=!4m2!3m1!1s0x0:0x5c5832cf826e6827?ved=2ahUKEwjSrKin3vreAhUJ-6QKHR96CtUQ_BIwDnoECAIQCA")

    elif message.content == "15":

        await client.send_message(message.channel, "This is our impressive Multi-storey car park, opened for staff and visitors in 2010. It has 457 spaces over 15 floors, including spaces for electric vehicles.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/dir/52.4099584,-1.5056896/Multi-Storey+Car+Park,+Coventry+University,+65-66+Gosford+St,+Coventry+CV1+5DL/@52.4081241,-1.5073421,16z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x48774bc7f4552951:0x67f58908f416574f!2m2!1d-1.49966!2d52.40625?hl=pt-PT")

    elif message.content == "16":

        await client.send_message(message.channel, "Built in 1964, this building is occupied by the Cambridge Education Group, who run their Foundation Campus from here. They offer University Pathway courses for foreign students who wish to gain entry to UK Universities. Also in this building is a large sports hall, and the University’s Student Union Radio.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/dir//Priory+Building,+Coventry+University,+Priory+Building,+Coventry+CV1+5FJ/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x48774bb963d4f237:0x89ecb9de30701a9c?ved=2ahUKEwiJxtHf4freAhXSzKQKHc6KBUEQ48ADMAB6BAgAEBc")

    elif message.content == "17":

        await client.send_message(message.channel, "This was built in 1971 and has been named after the political journalist and Labour politician, representing Coventry East from 1945-1974. This is the main building for the Faculty of Health and Life Sciences and includes a mock hospital ward and operating theatre, complete with sink scrubs and theatre lights.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Richard+Crossman+Building,+Coventry+University/@52.4066513,-1.5051487,15z/data=!4m5!3m4!1s0x0:0x7e3e53d31fa0f29f!8m2!3d52.4066513!4d-1.5051487")

    elif message.content == "18":

        await client.send_message(message.channel, "Built in 2017, the new facility was opened by the Duke and Duchess of Cambridge in January 2018. The £59m building allows students to learn to care for a patient at every stage of their healthcare experience.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Alison+Gingell+building/@52.4054596,-1.5039457,15z/data=!4m2!3m1!1s0x0:0xf32be84896390d38?ved=2ahUKEwiEr7m34vreAhXLGuwKHQMsB8kQ_BIwDnoECAYQCA")

    elif message.content == "19":

        await client.send_message(message.channel, "This building was built in 1970, and was named after the knighted British entrepreneur in the construction industry. This building is primarily used by the Faculty of Engineering, Environment and Computing, offering courses relating to the construction industry.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Sir+John+Laing+Building,+Coventry+University/@52.4058614,-1.5049971,15z/data=!4m2!3m1!1s0x0:0xeafa1753c3a2eb08?ved=2ahUKEwjh27_b4vreAhXssaQKHeUIBLkQ_BIwDnoECAEQCA")


    elif message.content == "20":

        await client.send_message(message.channel, "Constructed in 1980, this building is home to our IT services. Sir William Lyons was the co-founder of the Swallow Sidecar Company which subsequently became Jaguar Cars Limited.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Sir+William+Lyons+Building,+Coventry+University/@52.407352,-1.499745,15z/data=!4m2!3m1!1s0x0:0xd753684d34d8bb02?ved=2ahUKEwjxq_ae4_reAhWKGuwKHVmGDbwQ_BIwDnoECAYQCA")

    elif message.content == "21":

        await client.send_message(message.channel, "Construction was completed in 2006, and as its name suggests is home to some key student services as well as our International Office. This is where our students enroll as well as the main information point for student accommodation and finance queries.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Student+Centre+Building,+Coventry+University/@52.404955,-1.50074,15z/data=!4m5!3m4!1s0x0:0xf4c89a96d82bd7d7!8m2!3d52.404955!4d-1.50074")

    elif message.content == "22":

        await client.send_message(message.channel, "This is a small office used by our Faculty of Health and Life Sciences. Built in 1922 and its name is drawn from the Carmelite Friary founded in 1342 in Coventry.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/dir//Whitefriars+Building,+Coventry+University,+62+Whitefriars+St,+Coventry+CV1+2DS/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x48774bb9c6c49799:0xed3609e1c9fd66fb?ved=2ahUKEwjDjdrN4_reAhWwsaQKHYtdAzgQ48ADMAB6BAgFECU")

    elif message.content == "23":

        await client.send_message(message.channel, "This building began life in 1910 as a factory and has been named after the founder of the Morris car company who used this building as part of its engine production unit. It was converted for use by the University and is now occupied by our Faculty of Business and Law. ")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/William+Morris+Building,+Coventry+University/@52.406556,-1.5011871,15z/data=!4m2!3m1!1s0x0:0x47154db87f3ce74c?ved=2ahUKEwiirZrj4_reAhUIGuwKHf_qCUQQ_BIwDnoECAYQCA")

    elif message.content == "24":

        await client.send_message(message.channel, "Our own Sports and Recreation Centre offers a wide range of activities for all sporting tastes, available for use by Staff and Students. Most of the University accommodation includes free membership to the Centre.")

        await client.send_message(message.channel, "If you would like to visit this building the link for it's location is down below:")

        await client.send_message(message.channel, "https://www.google.co.uk/maps/place/Sport+and+Recreation+Centre/@52.4057853,-1.5042181,15z/data=!4m2!3m1!1s0x0:0xecbabd0c35133bce?ved=2ahUKEwjpw9X44_reAhVI26QKHQ4XDCkQ_BIwCnoECAYQCA")


client.run("NTAzNjU2MTc3NjgzMzk4Njc1.Dq5txg.WDWMGBovm-6VOTP86Nipck5YOcw")