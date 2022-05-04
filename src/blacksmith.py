from location import *
from CreateCharacters import *
from Items import *
from action import action

def placeBlacksmith():
    action('EnableIcon("Talk",talk,'+Gollum.name+',"Buy Sword",true)')
    action('EnableIcon("Exit",exit,'+Blacksmith.name+'.Door,"Exit Blacksmith",true)')
    action('Enter('+Harry.name+','+Blacksmith.name+'.Door,true)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')