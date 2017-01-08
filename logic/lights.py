from settings import *

lightWords = ['lights', 'light', 'on', 'off']

def turnLightsOn():
    return 0

def turnLightsOff():
    return 0

def lights(words):
    if 'off' in words:
        turnLightsOff()
    elif 'on' in words:
        turnLightsOn()
    elif settings_lights == 'on':
        turnLightsOff()
        settings_lights = 'off'
    else:
        turnLightsOn()
        settings_lights = 'on'

    # TODO - hook up lights
    if (settings_levelTwoAudibleConfirmations):
        return 'lights ' + settings_lights
    else:
        return ''
