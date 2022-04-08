from location import *
from CreateCharacters import *
from action import action


def placeLibrary():
    action('EnableIcon("Talk",talk,'+Librarian.name+',"Talk about Palpatine",true)')
    # action('EnableIcon("Pick",draw,'+Scroll.name+',"Pick up scroll",true)')
    action('FadeIn()')
    action('Enter('+Harry.name+','+Library.name+'.Door)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')