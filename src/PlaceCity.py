from Locations import *
from CreateCharacters import *
from action import action


def placeCity():
    action('EnableIcon("Enter",exit,'+City.name+'.GreenHouseDoor,"Enter Library",true)')
    action('FadeIn()')
    action('Enter('+Harry.name+','+City.name+'.EastEnd)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
