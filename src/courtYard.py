from action import action
from create_Character import Create_Character
from Narrator import Narrate

#Create Characters for CourtYard
security1=Create_Character('security1','A','LightArmour','Spiky','neutral')
security2=Create_Character('security2','B','LightArmour','Long','neutral')

def CourtYard(Char,place):
    Narrate("Exiting Castle and Entering Court Yard")
    action('SetPosition('+security1.name+','+place.name+'.RightBench)')
    action('SetPosition('+security2.name+','+place.name+'.LeftBench)')
    action('Sit('+security1.name+','+place.name+'.RightBench.Right)')
    action('Sit('+security2.name+','+place.name+'.LeftBench.Left)')
    action('EnableIcon("Exit",exit,'+place.name+'.Exit,"Exit Court Yard",true)')
    action('EnableIcon("Enter",exit,'+place.name+'.Gate,"Enter Castle",true)')
    Narrate.Hide_Narration()
    action('FadeIn()')
    action('Enter('+Char.name+','+place.name+'.Gate)')
    action('SetCameraFocus('+Char.name+')')
    action('SetCameraMode(follow)')
    Narrate("Completed Level-1. To be Continued....")
    action('Wait(3)')
    Narrate.Hide_Narration()