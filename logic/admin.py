from settings import *

notRecognizedResponses = {
    'DEFAULT': ['I\'m sorry, I don\'t know what you are saying',
    'I don\'t understand'],
    'FUNNY': ['What are you trying to say human?'],
}

def commandNotRecognized(words):
    response = notRecognizedResponses['DEFAULT']
    if settings_mood in notRecognizedResponses:
        response = notRecognizedResponses[settings_mood]

    return response