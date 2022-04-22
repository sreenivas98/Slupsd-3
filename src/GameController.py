from location import *
from CreateCharacters import *
from Items import *
from action import action
from Text import Text
from Narrator import Narrate
from GreatHall1 import *
from GreatHall2 import *
from PlaceCity import *
from CourtYard2 import *
from library import *


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
    create_characters()
    create_locations()
    Create_Item()
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
           action('WalkTo('+Harry.name+','+Castle_Moore.name+'.Gate)')
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
            action('Pickup('+Librarian.name+',Scroll,'+Library.name+'.AlchemistTable.Left)')
            action('WalkTo('+Librarian.name+','+Harry.name+')')
            action('Give('+Librarian.name+',Scroll,'+Harry.name+')')
            action('AddToList(Scroll,"Scroll - contains information about Palpatine")')
            action('ShowList('+Harry.name+')')
            action('EnableInput()')

        elif received == 'input Pick GoldBag':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Storage.name+'.Shelf)')
            action('Pickup('+Harry.name+',GoldBag,'+Storage.name+'.Shelf)')
            action('AddToList(GoldBag,"Gold coins bag - used to buy weapons from Blacksmith")')
            action('ShowList('+Harry.name+')')
            action('EnableInput()')
            
        elif received == 'input Pick GoldCup':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Storage.name+'.Shelf)')
            action('Pickup('+Harry.name+',GoldCup,'+Storage.name+'.Shelf)')
            action('AddToList(GoldCup,"Gold Cup - used to buy potions from Alchemist")')
            action('ShowList('+Harry.name+')')
            action('EnableInput()')
            
        elif received == 'input Close List':
            action('HideList()')

if __name__ == "__main__":
    main()