from location import *
from CreateCharacters import *
from action import action

def CourtYard():
    #action('EnableIcon("Exit",exit,'+Moore_Courtyard.name+'.Exit,"Exit Court Yard",true)')
    action('EnableIcon("Talk",talk,'+CYWorker.name+',"Talk about Kidnapping",true)')
    action('FadeIn()')
    action('Enter('+Harry.name+','+Moore_Courtyard.name+'.Gate)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
