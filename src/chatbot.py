import random

# ATL Slang Responses
atl_responses = [
    "Ayy bruh, you talkin' reckless! 😂",
    "Man, you sound confused as hell. Let me bless you real quick!",
    "You really out here wildin’, huh?",
    "Pssh, boy if you don't get...",
    "Bruh, ain't no way you just said that! 😆"
]

def get_response(user_input):
    """Returns a random ATL-style response."""
    return random.choice(atl_responses)

