import random
from settings import *
from language import *

helloWords = ['hello', 'hi', 'hey']
goodbyeWords = ['goodbye', 'bye', 'later', 'good', 'bye', 'see', 'you', 'by']
greetingWords = helloWords + goodbyeWords

helloResponses = {
    'DEFAULT': ['hello', 'hi', 'hey'],
    'PARTY': ['oh what up', 'yo yo yo yo'],
    'FUNNY': ['beep boop bop'],
}

helloResponses = {
    'DEFAULT': ['goodbye', 'bye'],
    'PARTY': ['later dog', 'see you on the flippity flop'],
    'FUNNY': ['bop beep beep'],
}

def greeting(words):
    helloCount = goodbyeCount = 0
    for word in words:
        if word in helloWords:
            helloCount += 1
        elif word in goodbyeWords:
            goodbyeCount += 1

    if helloCount > goodbyeCount:
        return hello(words)
    else:
        return goodbye(words)

def hello(words):
    mood = settings_mood
    response = random.choice(helloResponses['DEFAULT'])
    if mood in helloResponses:
        response = random.choice(helloResponses[mood])

    if (isRude(words) and (mood == 'FUNNY' or mood == 'DEFAULT')):
        response += randomInsult()

    return response

def goodbye(words):
    mood = settings_mood
    response = random.choice(goodbyeResponses['DEFAULT'])
    if mood in helloResponses:
        response = random.choice(helloResponses[mood])

    if (isRude(words) and (mood == 'FUNNY' or mood == 'DEFAULT')):
        response += randomInsult()

    return response