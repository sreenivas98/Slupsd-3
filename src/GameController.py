from Locations import *
from CreateCharacters import *
from action import action
from Text import Text
from Narrator import Narrate
from GreatHall1 import *
from GreatHall2 import *
from PlaceCity import *
from CourtYard2 import *
from PlaceLibrary import *


def showMenu():
    action("ShowMenu()")
    # action("HideMenu()")
    action("EnableInput()")
    
def credit_close():
    while (True):
        rec=input()
        if rec=="input Close Credits":
            break 


def show_credit():
        action("SetCredits('MyExperienceManager')")
        action("ShowCredits")
        credit_close()
        action("HideCredits")

def main():
    
    # intializations()
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    showMenu()

    # while listen_input():
    #     pass            

    while (True):
        
        received=input()

        # Menu interaction inputs
        if received=="input Selected Start":
            action('FadeOut()')
            action('HideMenu()')
            Great_hall()

        elif received=="input Selected Resume":
            action("HideMenu()")
            action("EnableInput()")

        elif received=="input Selected Credits":
            show_credit()
        
        elif received=="input Selected Quit":
            action("Quit()")          
        
        elif received=="input Key Pause":
            action("ShowMenu()")
        
        # General story interaction inputs
        elif received=="input Close Narration":
            # action("Quit()")
            action("HideNarration()")
            action("EnableInput()")
       
        elif received=='input Close List': #Close inventory List
            action("HideList()")
            
        elif received == 'input Talk King Jonathan':
           action('DisableInput()')
           action('WalkTo('+Harry.name+','+King_Jonathan.name+')')
           action('SetLeft('+Harry.name+')')
           action('SetRight('+King_Jonathan.name+')')
           Text(Harry.name, "Your Highness! Princess is kidnapped")
           action('SetExpression('+King_Jonathan.name+', angry)')
           Text(King_Jonathan.name, "What!! Who did that?")
           Text(Harry.name, "Palpatine did that and escaped")
           Text(King_Jonathan.name, "I will go and search for princess")
           Text(Harry.name, "No sir it is risky we will go and find the princess.")
           Text(King_Jonathan.name, "Okay! Don't forget to kill that bastard")
           action('SetLeft(null)')
           action('SetRight(null)')
           action('DisableIcon("Talk",'+King_Jonathan.name+')')
           action('EnableInput()')
           
        elif received == 'input Exit Castle_Moore.Gate':
           #action('OpenFurniture('+Char2.name+', '+Place1.name+'.Gate)')
           action('WalkTo('+Harry.name+',)')
           action('Exit('+Harry.name+', '+Castle_Moore.name+'.Gate)')
           action('FadeOut()')
           CourtYard()
           
        elif received == 'input Enter Castle_Moore.BasementDoor':
           action('Exit('+Harry.name+','+Castle_Moore.name+'.BasementDoor)')
           action('FadeOut()')
           placeStorage()  
           
        elif received == 'input Exit Storage.Door':
            action('Exit('+Harry.name+','+Storage.name+'.Door)')
            action('FadeOut()')
            Great_hall2()
        
        elif received == 'input Talk CYWorker':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+CYWorker.name+')')
            action('SetLeft('+CYWorker.name+')')
            action('SetRight('+Harry.name+')')
            Text(Harry.name, "What happened? Why are you scared?")
            action('SetExpression('+Harry.name+',surprised)')
            Text(CYWorker.name, "General Harry! I saw Palpatine take the princess into the city.")
            Text(Harry.name,"What? Are you sure?")
            Text(CYWorker.name, "Yes my Lord.")
            Text(Harry.name, "Go home. We will bring back the princess safely")
            action('SetLeft(null)')
            action('SetRight(null)')
            action('DisableIcon("Talk",'+CYWorker.name+')')
            action('WalkTo('+Harry.name+','+Moore_Courtyard.name+'.Exit)')
            action('FadeOut()')
            placeCity()
            
        elif received == 'input Enter city.GreenHouseDoor':
            action('DisableInput()')
            action('Exit('+Harry.name+','+City.name+'.GreenHouseDoor)')
            action('FadeOut()')
            placeLibrary()
            
        elif received == 'input Talk Librarian':
            action('DisableInput()')
            action('WalkTo('+Librarian.name+','+Harry.name+')')
            action('SetLeft('+Harry.name+')')
            action('SetRight('+Librarian.name+')')
            Text(Librarian.name, "Hello General! How may I help you?")
            action('SetExpression('+Harry.name+',angry)')
            Text(Harry.name, "Hello! I need some information about Palpatine")
            Text(Librarian.name,"Sure General! Palpatine has been the biggest criminal for a very long time")
            Text(Harry.name, "I know! He kidnapped our princess and took her somewhere.")
            action('SetExpression('+Librarian.name+',surprised)')
            Text(Librarian.name,"What??")
            Text(Harry.name, "I need more information on Palpatine to save our princess.")
            Text(Librarian.name,"Sure General! I have scroll that contains his details")
            action('SetLeft(null)')
            action('SetRight(null)')
            action('DisableIcon("Talk",'+Librarian.name+')')
            action('WalkTo('+Librarian.name+','+Library.name+'.AlchemistTable.Left)')
            # action('Pickup('+Librarian.name+','+Scroll2.name+','+Library.name+'.AlchemistTable.Left)')
            action('WalkTo('+Librarian.name+','+Harry.name+')')
            # action('Give('+Librarian.name+','+Scroll2+','+Harry.name+')')
            action('SetLeft('+Librarian.name+')')
            action('SetRight('+Harry.name+')')
            action('SetExpression('+Librarian.name+',neutral)')
            Text(Librarian.name, "Palpatine used to be a farmer and a respected person in this village.")
            Text(Librarian.name,"But! due to his greed he tried to steal gold coins from the king and got banished from this kingdom.")
            Text(Librarian.name, "Now he lives in a dungeon at the city outskirts. You will have to cross a Spooky path with thorns to each the dungeon.")
            Text(Librarian.name,"One more thing\, The Spooky path is guarded by the Gollum\, a very powerful man in this kingdom.")
            Text(Harry.name,"Thank you for the information.")
            action('SetLeft(null)')
            action('SetRight(null)')
            action('EnableInput()')
            # action('')
            # action('FadeOut()')
        

# while(True):
	# i = input()
	# if i == 'input Selected Start':
		# action('HideMenu()')
		# action('EnableInput()')
		# action('FadeOut()')
		# Narrate('Welcome to "The Kidnapping in Moore City"')
		# action('Wait(3)')
		# Narrate.Hide_Narration()
		# Great_hall()
		# CourtYard(Harry,Moore_Courtyard)
        
  
# Main Function starts here  
if __name__ == "__main__":
    main()