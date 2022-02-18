from ast import Return
from action import action
from courtYard import CourtYard
from Create_Item import item
from create_Character import Create_Character
from Text import Text
from Narrator import Narrate

#Create Guards
guard1=Create_Character('guard1','A','HeavyArmour','Spiky','neutral')
guard2=Create_Character('guard2','B','HeavyArmour','Long','neutral')
guard3=Create_Character('guard3','C','HeavyArmour','Spiky','neutral')
guard4=Create_Character('guard4','D','HeavyArmour','Short_Full','neutral')
guard5=Create_Character('guard5','E','HeavyArmour','Long','neutral')
guard6=Create_Character('guard6','F','HeavyArmour','Short_Full','neutral')

def Great_hall(Char1,Char2,Place1):
    Narrate('Welcome to "The Kidnapping in Moore City"')
    action('SetPosition('+Char1.name+','+Place1.name+'.Throne)')
    action('SetPosition('+guard1.name+','+Place1.name+'.RightBalcony)')
    action('SetPosition('+guard2.name+','+Place1.name+'.LeftBalcony)')
    action('SetPosition('+guard3.name+','+Place1.name+'.RightGuard)')
    action('SetPosition('+guard4.name+','+Place1.name+'.LeftGuard)')
    action('SetPosition('+guard5.name+','+Place1.name+'.LeftFoyer)')
    action('SetPosition('+guard6.name+','+Place1.name+'.RightFoyer)')
    action('Sit('+Char1.name+','+Place1.name+'.Throne)')
    action('EnableIcon("Talk",talk,'+Char1.name+',"Talk about princess",true)')
    action('EnableIcon("Exit",exit,'+Place1.name+'.Gate,"Exit Castle",true)')
    action('FadeIn()')
    Narrate.Hide_Narration()
    action('Enter('+Char2.name+','+Place1.name+'.Gate)')
    action('SetCameraFocus('+Char2.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
    action('SetExpression('+Char2.name+', sad)')
    while True:
       i = input()
       if i == 'input Talk King Jonathan':
           Text(Char2.name, "Your Highness, Princess is kidnapped")
           action('SetExpression('+Char1.name+', angry)')
           Text(Char1.name, "What!! Who did that?")
           Text(Char2.name, "Palpatine did that and escaped")
           Text(Char1.name, "I will go and search for princess")
           Text(Char2.name, "No sir, it is risky, we will go and find the princess.We got information that she is in the city")
           Text(Char1.name, "Okay, Don't forget to kill that bastard")
           action('DisableIcon("Talk",'+Char1.name+')')
       elif i == 'input Exit Castle_Moore.Gate':
           #action('OpenFurniture('+Char2.name+', '+Place1.name+'.Gate)')
           action('Exit('+Char2.name+', '+Place1.name+'.Gate)')
           action('FadeOut()')
           return





        #    action('Exit('+Char1.name+', '+Place1.name+'.Gate)')
        #    action('OpenFurniture('+Char1.name+', '+Place1.name+'.Gate)')
        #    action('FadeOut()')
        #    action('FadeIn()')
        #    action('Enter('+Char2.name+','+Place2.name+'.Gate)')
        #    action('EnableInput()')









