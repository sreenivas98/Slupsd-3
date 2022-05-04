from location import *
from CreateCharacters import *
from Items import *
from action import action

def placeAlchemyShop():
    action('EnableIcon("Talk",talk,'+Alchemist.name+',"Buy potion",true)')
    action('EnableIcon("Exit",exit,'+Alchemy.name+'.Door,"Exit Blacksmith",true)')
    action('Enter('+Harry.name+','+Alchemy.name+'.Door,true)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')