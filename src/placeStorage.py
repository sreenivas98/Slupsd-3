from location import *
from CreateCharacters import *
from Items import *
from action import action

def placeStorage():
    action('EnableIcon("Pick",draw,GoldBag,"Pick GoldBag",true)')
    action('EnableIcon("Pick",draw,GoldCup,"Pick GoldCup",true)')
    action('FadeIn()')
    action('Enter('+Harry.name+','+Storage.name+'.Door)')
    action('EnableIcon("Exit",exit,'+Storage.name+'.Door,"Exit Storage",true)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
    action('SetExpression('+Harry.name+', angry)')

