from location import *
from CreateCharacters import *
from Items import *
from action import action

def placeForest():
    action('EnableIcon("Talk",talk,'+Stranger.name+',"Enter camp",true)')
    action('Enter('+Harry.name+','+Forest.name+'.EastEnd,true)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
