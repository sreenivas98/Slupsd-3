from action import action
from Create_Item import item
from Text import Text

def Great_hall(King_Jonathan,Harry,Castle_Moore,Moore_Courtyard):
    action('SetPosition('+King_Jonathan.name+','+Castle_Moore.name+'.Throne)')
    action('Sit('+King_Jonathan.name+','+Castle_Moore.name+'.Throne)')
    action('OpenFurniture('+Harry.name+', '+Castle_Moore.name+'.Gate)')
    action('CloseFurniture('+Harry.name+', '+Castle_Moore.name+'.Gate)')
    action('Enter('+Harry.name+','+Castle_Moore.name+'.Gate)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
    action('WalkTo('+Harry.name+','+King_Jonathan+')')
    Text(Harry.name, 'Your Highness,Princess is kidnapped')
    action('SetExpression('+Harry.name+', sad)')
    Text(King_Jonathan.name, 'What!!Who did that?')
    action('SetExpression('+King_Jonathan.name+', angry)')
    Text(Harry.name, 'Papatine did that and escaped')
    Text(King_Jonathan.name, 'I will go and search for princess')
    Text(Harry.name, 'No sir, it is risky, we will go and find the princess.We got information that she is at city')
    Text(King_Jonathan.name, 'No,I will go kill papatine and rescue the princess')
    action('Exit('+King_Jonathan.name+', '+Castle_Moore.name+'.Gate)')
    action('OpenFurniture('+King_Jonathan.name+', '+Castle_Moore.name+'.Gate)')
    action('FadeOut()')
    action('FadeIn()')
    action('Enter('+Harry.name+','+Moore_Courtyard.name+'.Gate)')
    action('EnableInput()')







