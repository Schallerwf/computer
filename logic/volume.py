lowerWords = ['down', 'lower', 'quieter']
higherWords = ['up', 'higher', 'louder']
muteWords = ['mute', 'shutup', 'quiet', 'callete', 'be', 'quiet', 'no', 'sound', 'zip', 'it', 'stop', 'halt', 'pause', 'off']
volumeWords = ['volume', 'set', 'turn', 'it'] + muteWords + lowerWords + higherWords

def volume(words):
    volumeScore = 0
    muteScore = 0
    for word in words:
        if word in volumeWords:
            volumeScore += 1
        elif word in muteWords:
            muteScore += 1

    if muteScore > volumeScore:
        settings_volume = 0
    else:
        lowerScore = 0
        higherScore = 0
        for word in words:
            if word in lowerWords:
                lowerScore += 1
            elif word in higherWords:
                higherScore += 1

        number = getNumberFromString(words)

        if higherScore or lowerScore > 1:
            if higherScore > lowerScore:
                settings_volume += number
            else:
                settings_volume -= number
        else:
            settings_volume = number

    if settings_levelTwoAudibleConfirmations:
        return 'volume set to ' + numberToString(number)
    else:
        return ''