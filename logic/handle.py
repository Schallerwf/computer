import copy

from language import *
from mute import *
from greetings import *
from lights import *
from volume import *
from admin import *
from settings import *
from speak import *

commands = {
    volume: volumeWords,
    greeting: greetingWords,
    lights: lightWords,
    }

def isMessageForComputer(words, numWords):
    if (words[0] in language_wakeWords):
        return True

    if (numWords > 1 and words[1] in language_wakeWords):
        return True

    if (numWords > 2 and words[2] in language_wakeWords):
        return True

    return False

def processWords(words):
    processedWords = []
    for word in words:
        if (word not in language_politeWords and word not in language_rudeWords):
            processedWords.append(word)

    return processedWords

def calculateScore(commandWords, inputWords):
    matches = 0
    for word in inputWords:
        if word in commandWords:
            matches += 1
    return matches

def handle(message):
    message = message.lower()
    words = message.split(' ')
    processedWords = processWords(words)

    numWords = len(words)
    numProcessedWords = len(processedWords)

    execute = lambda: commandNotRecognized(words)
    maxScore = settings_minThreshold

    if (numWords > 1 and isMessageForComputer(processedWords, numProcessedWords)):
        for key, value in commands.items():
            score = calculateScore(value, processedWords)

            if (score > maxScore):
                command = copy.copy(key)
                args = copy.copy(words)
                execute = lambda: command(args)
                maxScore = score

        vocalResponse = execute()
        if settings_levelOneAudibleConfirmations:
            speak(vocalResponse)