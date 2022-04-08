from Locations import *
from CreateCharacters import *

def Great_hall2():
    Narrate('Entering into Throne room')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    # action('Enter('+Harry.name+','+Castle_Moore.name+'.Gate)')
    # action('FadeIn()')
    # action('Enter('+Harry.name+','+Castle_Moore.name+'.Gate)')
    # action('EnableInput()')
    action('SetExpression('+Harry.name+', sad)')
    action('EnableIcon("Exit",exit,'+Castle_Moore.name+'.Gate,"Exit Castle",true)')
    action('EnableIcon("Talk",talk,'+King_Jonathan.name+',"Talk about princess",true)')
    action('FadeIn()')
    action('Enter('+Harry.name+','+Castle_moore.name+'.BasementDoor)')
    action('EnableIcon("Enter",exit,'+Castle_Moore.name+'.BasementDoor,"Enter Storage",true)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
    action('SetExpression('+Harry.name+', sad)')