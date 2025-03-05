import random

# ATL-style Roasts
roasts = [
    "Bruh, you so broke, your wallet got cobwebs! 💀😂",
    "Boy, yo haircut look like it was drawn in MS Paint! 😂",
    "You so slow, you took a week to reply to a text!😂",
    "Bruh, you built like a melted candle. 😭",
    "Boy, you dress like Goodwill had a clearance sale!😂",
    "Bruh, your personality's as dry as the Sahara! 🏜️😂",
    "You so dumb, you tried to climb a glass wall! 🤦🏾‍♂️😂",
    "You out here lookin' like you were raised by a Wi-Fi router. 😆😂",
    "Man, you wear the same shoes your grandma gave you for Christmas. 👟😂",
    "Bruh, you a whole snack... if the snack was expired. 🍪😂",
    "You the human version of a participation trophy. 🏆😂",
    "You a walking definition of 'failure with a chance of success.' 🤷🏾‍♂️😂",
    "Is that your face, or is your neck blowing a bubble? 😂",
    "Bruh, you ain't got a clue what you're doing, and it shows. 🤣",
    "Boy, your brain’s so empty it echoes. 🧠😂",
    "You more confusing than a GPS that doesn’t work. 🧭😂",
    "Your drip is as dry as the desert, fam. 🌵😂",
    "If laziness was a sport, you'd be an Olympic gold medalist. 🥇😂",
    "You out here acting like a snack when you barely a cracker. 🧀😂",
    "Boy, you the kind of person that gets a participation trophy just for showing up. 🏅😂",
    "Bruh, you so lost, you make Google Maps look bad. 📱😂",
    "Man, you got more excuses than a lazy teenager. 📺😂",
    "Your vibe is as depressing as a rainy Monday. 🌧️😂",
    "If there was a contest for acting clueless, you'd be the judge. 🤦🏽‍♀️😂",
    "You look like you hit the snooze button on life. ⏰😂",
    "Man, you're the reason they say 'beauty is skin deep.' 😬😂",
    "You a whole clown but without the circus. 🤡😂",
    "Bro, your dreams are so small they fit in a shoebox. 📦😂",
    "You talk like you got knowledge, but I see a blank page. 📖😂",
    "Your vibe is like a broken pencil—pointless. ✏️😂",
    "You look like you just got out of a wet paper bag. 💧😂",
    "You the kind of person who'd lose at Monopoly... with no money. 💸😂",
    "Bruh, your breath smells like you’ve been chewing on your problems. 😷😂",
    "You built like a lollipop... all stick, no flavor. 🍭😂",
    "You got the energy of a wet sponge. 💦😂",
    "You’re like a cloud—when you disappear, it’s a good day. ☁️😂",
    "If you were a vegetable, you’d be a ‘couch potato.’ 🥔😂",
    "Your sense of humor is like a broken TV—no signal. 📺😂",
    "You walk into a room and people think 'uh-oh, here we go'. 🤦🏽‍♂️😂",
    "Bruh, your existence is as confusing as your profile picture. 🤔😂",
    "You built like a beach chair—folded under pressure. 🪑😂",
    "You out here looking like the human version of a typo. 📝😂",
    "Man, you the human embodiment of 'meh.' 😐😂",
    "You can’t even spell 'success' without a struggle. 📚😂",
    "If ignorance was a superpower, you'd be a hero. 🦸🏾‍♂️😂",
    "You so slow, even a snail's got more hustle. 🐌😂",
    "You look like a spam email. 📨😂",
    "Bruh, you out here acting like you’re famous... but still stuck in the 2000s. 📼😂",
    "Your personality's like a horror movie—nobody wants to deal with it. 🎃😂",
    "You sound like you Googled 'how to roast' and just copied the first result. 💻😂",
    "Bruh, you're like Wi-Fi—only useful when you're close enough. 📶😂",
    "You look like a glitch in the matrix. 💻😂",
    "If I had a dollar for every time you messed up, I'd be richer than your self-esteem. 💸😂",
    "You got the vibe of a missing sock—lost and never found. 🧦😂",
    "You out here like a malfunctioning vending machine—no one knows what you're about. 🍫😂",
    "Your energy is like dial-up internet—slow, frustrating, and outdated. 🖥️😂"
    "Bruh, you so broke, even your shadow won’t follow you no more! 💀😂"
    "Boy, your barber been playing tic-tac-toe on your head! 😂"
    "You so slow, you took a nap in the middle of a race! 🏁😂"
    "Bruh, you built like an expired marshmallow—soft and irrelevant. 😭😂"
    "Boy, you got a personality as exciting as a blank spreadsheet. 📊😂"
    "You so dumb, you thought a quarterback was a refund. 🏈😂"
    "You out here lookin' like you still waiting for puberty to call you back. 📞😂"
    "Man, your Wi-Fi signal got more bars than your sense of humor. 📶😂"
    "Bruh, you a whole snack… if the snack was moldy bread. 🍞😂"
    "You got the confidence of a Windows update—nobody asked for it. 💻😂"
 
]

def get_roast():
    """Returns a random ATL-style roast."""
    return random.choice(roasts)

