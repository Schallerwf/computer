from settings import *
import random

language_wakeWords = ['computer']
language_politeWords = ['please', 'thanks', 'sorry', 'thank', 'por', 'favor']
language_rudeWords = ['fuck', 'shit', 'bitch']

insults = ['stupid human', 'idiot', 'meat bag']

def isRude(words):
    score = 0
    for word in words:
        if word in language_rudeWords:
            score += 1

    if (score >= rudeThreshold):
        return True
    return False

def randomInsult():
    return random.choice(insults)