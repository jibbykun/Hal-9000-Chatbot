        elif message.content == "Hal" or message.content == "hal":
            await client.send_message(message.channel, "Yes?",tts=True) 
        elif message.content == ":joy:" or message.content == ":smile:":
            await client.send_message(message.channel, ":ok_hand:",tts=True)
        elif message.content == "Link me to google" or message.content == "google" or message.content == "Google":
            await client.send_message(message.channel, "Here's the link to Google: https://www.google.co.uk/",tts=True)
        elif message.content == "Can you redirect me to the university website?" or message.content == "link to coventry university":
            await client.send_message(message.channel, "Sure. Just click on this link: https://www.coventry.ac.uk/",tts=True)
        elif message.content == "LinkedIn" or message.content == "linkedin":
            await client.send_message(message.channel, "Here's the link to LinkedIn: https://www.linkedin.com/",tts=True)
        elif message.content == "GitHub" or message.content == "github":
            await client.send_message(message.channel, "Here's the link to GitHub: https://github.coventry.ac.uk/",tts=True)
        elif message.content == "Youtube" or message.content == "youtube":
            await client.send_message(message.channel, "Here's the link to Youtube: https://www.youtube.com/",tts=True)
        elif message.content == "Facebook" or message.content == "facebook":
            await client.send_message(message.channel, "Here's the link to Facebook: https://www.facebook.com/",tts=True)
        elif message.content == "Can you send me a website link?" or message.content == "can you send me a website link?":
            await client.send_message(message.channel, "Of course. Which website link do you need?",tts=True)
