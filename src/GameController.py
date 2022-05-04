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
from Climax import *
from AlchemyShop import *
from Blacksmith import *
from Forest import *


def showMenu():
    action("SetTitle('Kidnapping in Moore City')")
    action('ShowMenu()')
    # action("HideMenu()")
    action('EnableInput()')
    
def credit_close():
    while (True):
        rec=input()
        if rec=="input Close Credits":
            break 


def show_credit():
        action("SetCredits('Kidnapping in Moore City')")
        action("ShowCredits()")
        credit_close()
        action("HideCredits")
        
def setBagFlag():
    global bagFlag
    bagFlag=True

def setCupFlag():
    global cupFlag
    cupFlag=True

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
            showMenu()
        
        # General story interaction inputs
        elif received=="input Close Narration":
            # action("Quit()")
            action('DisableInput()')
            Narrate.Hide_Narration()
            # action("HideNarration()")
            action("EnableInput()")
       
        elif received=='input Close List': #Close inventory List
            action("HideList()")
            
        elif received == 'input Talk King Jonathan':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+King_Jonathan.name+')')
            action('SetLeft('+Harry.name+')')
            action('SetRight('+King_Jonathan.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Harry.name+' : Your Highness! Princess is kidnapped")')
            action('Wait(2)') 
            action('SetExpression('+King_Jonathan.name+', angry)')
            action('SetDialog("'+King_Jonathan.name+' : What!! Who did that?")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : Palpatine did that and escaped")')
            action('Wait(2)') 
            action('SetDialog("'+King_Jonathan.name+' : I will go and search for princess")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : No sir it is risky we will go and find the princess.")')
            action('Wait(2)') 
            action('SetDialog("'+King_Jonathan.name+' : Okay! Do not forget to kill that bastard")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('DisableIcon("Talk",'+King_Jonathan.name+')')
            global talkFlagKing
            talkFlagKing=True
            action('SetCameraFocus('+Harry.name+')')
            action('SetCameraMode(follow)')
            action('EnableInput()')
            
        elif received == 'input Talk Palpatine':
            action('DisableInput()')
            action('WalkTo('+Palpatine.name+','+Harry.name+')')
            action('SetLeft('+Harry.name+')')
            action('SetRight('+Palpatine.name+')')
            action('SetExpression('+Harry.name+',angry)')
            action('ShowDialog()')
            action('SetDialog("'+Harry.name+' : Bastard! Where is the princess?")')
            action('Wait(2)')
            action('SetExpression('+Palpatine.name+',angry)')
            action('SetDialog("'+Palpatine.name+' : Dog! I amgoing to kill you.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : Lets see who die first.")')
            action('Wait(2)')  
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('WalkTo('+Palpatine.name+','+Dungeon.name+'.Table)')
            action('PickUp('+Palpatine.name+',Sword_vill,'+Dungeon.name+'.Table)')
            action('WalkTo('+Palpatine.name+','+Harry.name+')')
            if HammerFlag == True:
                action('Draw('+Harry.name+',Hammer1)')
            elif SwordFlag == True:
                action('Draw('+Harry.name+',Sword1)')
            action('Attack('+Palpatine.name+','+Harry.name+')')
            action('Attack('+Harry.name+','+Palpatine.name+')')
            action('CreateEffect('+Palpatine.name+',Blood)')
            action('Die('+Palpatine.name+')')
            action('CreateEffect('+Palpatine.name+',Death)')
            action('EnableIcon("Open",exit,'+Dungeon.name+'.CellDoor,"Open cell door",true)')
            action('EnableInput()')
            
        elif received == 'input Open Dungeon.CellDoor':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Dungeon.name+'.CellDoor)')
            action('OpenFurniture('+Harry.name+','+Dungeon.name+'.CellDoor)')
            action('EnableIcon("Talk",talk,'+Princess_Scarlett.name+',"Talk with Princess",true)')
            action('EnableInput()')
            
        elif received == 'input Talk Princess Scarlett':
            action('EnableEffect('+Dungeon.name+',Peaceful)')
            action('SetCameraMode(track)')
            action('WalkTo('+Princess_Scarlett.name+','+Harry.name+')')
            action('SetExpression('+Princess_Scarlett.name+',happy)')
            action('SetRight('+Harry.name+')')
            action('SetLeft('+Princess_Scarlett.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Princess_Scarlett.name+' : Hello General! I am really happy to see you. I thought that I will die alone in this cell.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : No princess, Until we are there to protect you no one can harm you.")')
            action('Wait(2)') 
            action('SetDialog("'+Princess_Scarlett.name+' : Thank you general for saving me from this hell.")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('DanceTogether('+Harry.name+','+Princess_Scarlett.name+')')
            action('Wait(4)')
            Narrate('The End')
            action('Wait(3)')
            action('HideNarration()')
            show_credit()
            
        elif received == 'input Attack Palpatine':
            action('DisableInput()')
            action('WalkTo('+Palpatine.name+','+Harry.name+')')
            if HammerFlag == True:
                action('Draw('+Harry.name+',Hammer1)')
            elif SwordFlag == True:
                action('Draw('+Harry.name+',Sword1)')
            action('Attack('+Palpatine.name+','+Harry.name+')')
            action('Attack('+Harry.name+','+Palpatine.name+')')
            action('CreateEffect('+Palpatine.name+',Blood)')
            action('Die('+Palpatine.name+')')
            action('CreateEffect('+Palpatine.name+',Death)')
            action('EnableIcon("Open",exit,'+Dungeon.name+'.CellDoor,"Open cell door",true)')
            action('EnableInput()')
            
        elif received == 'input Talk Stranger2':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Stranger2.name+')')
            action('SetLeft('+Harry.name+')')
            action('SetRight('+Stranger2.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Harry.name+' : Hello! Have you seen anyone with a bandit outfit here.")')
            action('Wait(2)') 
            action('SetDialog("'+Stranger2.name+' : I have seen some guy with weapon running towards the forest.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : Are you sure?")')
            action('Wait(2)') 
            action('SetDialog("'+Stranger2.name+' : Yes my Lord.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : Thank you for providing the information.")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('WalkTo('+Harry.name+','+City.name+'.WestEnd)')          
            placeForest()
        
        elif received == 'input Talk Stranger':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Stranger.name+')')
            action('SetLeft('+Harry.name+')')
            action('SetRight('+Stranger.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Harry.name+' : Hello! Can i know why you are standing in my way.")')
            action('Wait(2)') 
            action('SetDialog("'+Stranger.name+' : You need to answer a riddle to cross me.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : I am in a hurry. Go ahead and tell me the riddle.")')
            action('Wait(2)') 
            action('SetDialog("'+Stranger.name+' : If a giraffe has two eyes, a monkey has two eyes, and an elephant has two eyes, how many eyes do we have?.")')
            action('SetDialog("[3|3]")')
            action('SetDialog("[2|2]")')
            action('SetDialog("[4|4]")')
            action('SetDialog("[1|1]")')
            action('EnableInput()')
        
        elif received == 'input Selected 4':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Stranger.name+')')
            action('SetLeft('+Stranger.name+')')
            action('SetRight('+Harry.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Stranger.name+' : You have given the correct answer. Take this armour as a reward.")')
            action('Wait(2)') 
            action('SetExpression('+Harry.name+',surprised)')
            action('SetDialog("'+Harry.name+' : Armour??")')
            action('Wait(2)') 
            action('SetDialog("'+Stranger.name+' : Yes! It will protect you against your enemies.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : Thank you for the generosity.")')
            action('Wait(2)')
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('SetCameraMode(track)')
            action('EnableEffect('+Stranger.name+',Aura)')
            action('Wait(2.5)')
            action('FadeOut()')
            action('SetClothing('+Harry.name+',HeavyArmour)')
            action('FadeIn()')
            action('WalkTo('+Harry.name+','+Forest.name+'.WestEnd)')
            placeFarm()
            
        elif received == 'input Selected 3' or received == 'input Selected 2' or received == 'input Selected 1':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Stranger.name+')')
            action('SetLeft('+Stranger.name+')')
            action('SetRight('+Harry.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Stranger.name+' : You have given the wrong answer. I will give you one more chance.")')
            action('Wait(2)') 
            # action('SetExpression('+Harry.name+',surprised)')
            action('SetDialog("'+Harry.name+' : Okay!")')
            action('Wait(2)') 
            action('SetDialog("'+Stranger.name+' : I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?")')
            action('SetDialog("[map|Map]")')
            action('SetDialog("[house|A house with pool and mountain view]")')
            action('EnableInput()')
         
        elif received == 'input Selected map':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Stranger.name+')')
            action('SetLeft('+Stranger.name+')')
            action('SetRight('+Harry.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Stranger.name+' : You have given the correct answer. Take this armour as a reward.")')
            action('Wait(2)') 
            action('SetExpression('+Harry.name+',surprised)')
            action('SetDialog("'+Harry.name+' : Armour??")')
            action('Wait(2)') 
            action('SetDialog("'+Stranger.name+' : Yes! It will protect you against your enemies.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : Thank you for the generosity.")')
            action('Wait(2)')
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('SetCameraMode(track)')
            action('EnableEffect('+Stranger.name+',Aura)')
            action('Wait(2.5)')
            action('FadeOut()')
            action('SetClothing('+Harry.name+',HeavyArmour)')
            action('FadeIn()')
            action('WalkTo('+Harry.name+','+Forest.name+'.WestEnd)')
            placeFarm()

        elif received == 'input Selected house':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Stranger.name+')')
            action('SetLeft('+Stranger.name+')')
            action('SetRight('+Harry.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Stranger.name+' : You have given the wrong answer. There are no more chances left.")')
            action('Wait(2)') 
            # action('SetExpression('+Harry.name+',surprised)')
            action('SetDialog("'+Harry.name+' : What? What are you going to do?")')
            action('Wait(2)') 
            action('SetDialog("'+Stranger.name+' : As you are not able to answer the riddles you are marked for death.")')
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('SetCameraMode(track)')
            action('CreateEffect('+Stranger.name+',Spiralflame)')
            action('CreateEffect('+Harry.name+',Blood)')
            action('DisableEffect('+Stranger.name+',Spiralflame)')
            action('Die('+Harry.name+')')
            action('EnableEffect('+Harry.name+',Death)')
            action('EnableInput()')
            
        elif received == 'input Pick GoldBag':
            action('DisableInput()')
            if bagFlag == False:
                action('WalkTo('+Harry.name+','+Storage.name+'.Shelf)')
                action('Pickup('+Harry.name+',GoldBag,'+Storage.name+'.Shelf)')
                action('AddToList(GoldBag,"Gold coins bag - used to trade for required items")')
                action('Pocket('+Harry.name+',GoldBag)')
                action('ShowList('+Harry.name+')')
                setBagFlag()
            else:
                action('Unpocket('+Harry.name+',GoldBag)')
            # action('ShowList('+Harry.name+')')
            # global bagFlag
            # bagFlag=True
            action('EnableInput()')
            
        elif received == 'input Pick GoldCup':
            action('DisableInput()')
            if cupFlag == False:
                action('WalkTo('+Harry.name+','+Storage.name+'.Shelf)')
                action('Pickup('+Harry.name+',GoldCup,'+Storage.name+'.Shelf)')
                action('AddToList(GoldCup,"Gold Cup - used to trade for required items")')
                action('Pocket('+Harry.name+',GoldCup)')
                action('ShowList('+Harry.name+')')
                setCupFlag()
            else:
                action('Unpocket('+Harry.name+',GoldCup)')
            action('EnableInput()')
            
        # elif received == ''
           
        elif received == 'input Exit Castle_Moore.Gate':
            if talkFlagKing==True and (bagFlag==True or cupFlag==True):
                action('DisableInput()')
                action('WalkTo('+Harry.name+','+Castle_Moore.name+'.Gate)')
                action('Exit('+Harry.name+', '+Castle_Moore.name+'.Gate,true)')                
                CourtYard()
            elif talkFlagKing==False:
                Narrate('You must talk to the king before leaving the castle.')
            elif bagFlag==False and cupFlag==False:
                Narrate('You may need some gold to buy weapons and potions. Gold is available in the storage room under the throne.')                
           
        elif received == 'input Enter Castle_Moore.BasementDoor':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Castle_Moore.name+'.BasementDoor)')
            action('Exit('+Harry.name+','+Castle_Moore.name+'.BasementDoor,true)')            
            placeStorage()  
           
        elif received == 'input Exit Storage.Door':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Storage.name+'.Door)')
            action('Exit('+Harry.name+','+Storage.name+'.Door,true)')            
            Great_hall2()
            
        elif received == 'input Talk Gollum':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Gollum.name+')')
            action('SetLeft('+Harry.name+')')
            action('SetRight('+Gollum.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Harry.name+' : Hello! I need to buy some weapons from you")')
            action('Wait(2)') 
            action('SetDialog("'+Gollum.name+' : Okay! which weapon do you need?")')
            action('Wait(2)') 
            action('SetDialog("[Hammer|Hammer]")')
            action('SetDialog("[Sword|Sword]")')
            action('EnableInput()')
            
        elif received == 'input Selected Hammer':
            action('DisableInput()')
            action('SetDialog("'+Harry.name+' : I need the hammer to smash the bastards head")')
            action('Wait(2)') 
            action('SetDialog("'+Gollum.name+' : Okay! let me get the hammer for you. I need gold coins to give you the weapon.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : I have a bag full of coins for you")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            setHammerFlag()
            action('DisableIcon("Talk",'+Gollum.name+')')
            action('Give('+Harry.name+',GoldBag,'+Gollum.name+')')
            action('RemoveFromList(GoldBag)')
            action('Pocket('+Gollum.name+',GoldBag)')
            action('WalkTo('+Gollum.name+','+Blacksmith.name+'.Table)')
            action('Pickup('+Gollum.name+',Hammer1,'+Blacksmith.name+'.Table)')
            action('WalkTo('+Gollum.name+','+Harry.name+')')
            action('Give('+Gollum.name+',Hammer1,'+Harry.name+')')
            action('AddToList(Hammer1,"Hammer - Weapon to kill someone by smashing")')
            action('ShowList('+Harry.name+')')
            action('EnableInput()')
        
        elif received == 'input Selected Sword':
            action('DisableInput()')
            action('SetDialog("'+Harry.name+' : I need the sword to cut the bastard in half")')
            action('Wait(2)') 
            action('SetDialog("'+Gollum.name+' : Okay! let me get the sword for you. I need gold coins to give you the weapon.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : I have a bag full of coins for you")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            setSwordFlag()
            action('DisableIcon("Talk",'+Gollum.name+')')
            action('RemoveFromList(GoldBag)')
            action('Pocket('+Gollum.name+',GoldBag)')
            action('WalkTo('+Gollum.name+','+Blacksmith.name+'.Table)')
            action('Pickup('+Gollum.name+',Sword1,'+Blacksmith.name+'.Table)')
            action('WalkTo('+Gollum.name+','+Harry.name+')')
            action('Give('+Gollum.name+',Sword1,'+Harry.name+')')
            action('AddToList(Sword1,"Sword - Weapon to kill someone by cutting")')
            action('ShowList('+Harry.name+')')
            action('EnableInput()')
            
        elif received == 'input Talk Alchemist':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Alchemist.name+')')
            action('SetLeft('+Harry.name+')')
            action('SetRight('+Alchemist.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Harry.name+' : Hello! I need to buy some potions from you")')
            action('Wait(2)') 
            action('SetDialog("'+Alchemist.name+' : Okay! which potion do you need?")')
            action('Wait(2)') 
            action('SetDialog("[RedPotion|Red Potion]")')
            action('SetDialog("[GreenPotion|Green Potion]")')
            action('EnableInput()')
            
        elif received == 'input Selected RedPotion':
            action('DisableInput()')
            action('SetDialog("'+Harry.name+' : I need the Red potion.")')
            action('Wait(2)') 
            action('SetDialog("'+Alchemist.name+' : Okay! I need gold item to give you the potion.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : I have a gold cup for you.")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('DisableIcon("Talk",'+Alchemist.name+')')
            action('Give('+Harry.name+',GoldCup,'+Alchemist.name+')')
            action('RemoveFromList(GoldCup)')
            action('Pocket('+Alchemist.name+',GoldCup)')
            action('WalkTo('+Alchemist.name+','+Alchemy.name+'.AlchemistTable)')
            action('Pickup('+Alchemist.name+',RedPotion1,'+Alchemy.name+'.AlchemistTable)')
            action('WalkTo('+Alchemist.name+','+Harry.name+')')
            action('Give('+Alchemist.name+',RedPotion1,'+Harry.name+')')
            action('Drink('+Harry.name+')')
            action('EnableInput()')            
            
        elif received == 'input Selected GreenPotion':
            action('DisableInput()')
            action('SetDialog("'+Harry.name+' : I need the Green potion.")')
            action('Wait(2)') 
            action('SetDialog("'+Alchemist.name+' : Okay! I need gold item to give you the potion.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : I have a gold cup for you.")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('DisableIcon("Talk",'+Alchemist.name+')')
            action('Give('+Harry.name+',GoldCup,'+Alchemist.name+')')
            action('RemoveFromList(GoldCup)')
            action('Pocket('+Alchemist.name+',GoldCup)')
            action('WalkTo('+Alchemist.name+','+Alchemy.name+'.Table)')
            action('Pickup('+Alchemist.name+',GreenPotion1,'+Alchemy.name+'.Table)')
            action('WalkTo('+Alchemist.name+','+Harry.name+')')
            action('Give('+Alchemist.name+',GreenPotion1,'+Harry.name+')')
            action('Drink('+Harry.name+')')
            action('EnableInput()') 
            
        elif received == 'input Exit Blacksmith.Door':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Blacksmith.name+'.Door)')
            action('Exit('+Harry.name+','+Blacksmith.name+'.Door,true)') 
            setCityFlagBs()
            placeCity2()
            
        elif received == 'input Exit Library.Door':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Library.name+'.Door)')
            action('Exit('+Harry.name+','+Library.name+'.Door,true)')            
            placeCity2()
            
        elif received == 'input Exit Alchemy.Door':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Alchemy.name+'.Door)')
            action('Exit('+Harry.name+','+Alchemy.name+'.Door,true)') 
            setCityFlagAs()
            placeCity2()
        
        elif received == 'input Talk CYWorker':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+CYWorker.name+')')
            action('SetLeft('+CYWorker.name+')')
            action('SetRight('+Harry.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Harry.name+' : What happened? Why are you scared?")')
            action('Wait(2)') 
            action('SetExpression('+Harry.name+',surprised)')
            action('SetDialog("'+CYWorker.name+' : General Harry! I saw Palpatine take the princess into the city.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : What? Are you sure?")')
            action('Wait(2)') 
            action('SetDialog("'+CYWorker.name+' : Yes my Lord.")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : Go home. We will bring back the princess safely")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('WalkTo('+Harry.name+','+Moore_Courtyard.name+'.Exit)')
            action('SetExpression('+Harry.name+',angry)')            
            placeCity()
            
        elif received == 'input Enter city.GreenHouseDoor':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+City.name+'.GreenHouseDoor)')
            action('Exit('+Harry.name+','+City.name+'.GreenHouseDoor,true)')            
            placeLibrary()
            
        elif received == 'input Enter city.BrownHouseDoor':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+City.name+'.BrownHouseDoor)')
            action('Exit('+Harry.name+','+City.name+'.BrownHouseDoor,true)')            
            placeBlacksmith()
            
        elif received == 'input Enter Farm.Door':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+Farm.name+'.Door)')
            action('Exit('+Harry.name+','+Farm.name+'.Door,true)')            
            placeDungeon()
            
        elif received == 'input Enter city.RedHouseDoor':
            action('DisableInput()')
            action('WalkTo('+Harry.name+','+City.name+'.RedHouseDoor)')
            action('Exit('+Harry.name+','+City.name+'.RedHouseDoor,true)')            
            placeAlchemyShop()
            
        elif received == 'input Talk Librarian':
            action('DisableInput()')
            action('WalkTo('+Librarian.name+','+Harry.name+')')
            action('SetLeft('+Harry.name+')')
            action('SetRight('+Librarian.name+')')
            action('ShowDialog()')
            action('SetDialog("'+Librarian.name+' : Hello General! How may I help you?")')
            action('Wait(2)') 
            action('SetExpression('+Harry.name+',angry)')
            action('SetDialog("'+Harry.name+' : Hello! I need some information about Palpatine")')
            action('Wait(2)') 
            action('SetDialog("'+Librarian.name+' : Sure General! Palpatine has been the biggest criminal for a very long time")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : I know! He kidnapped our princess and took her somewhere.")')
            action('Wait(2)') 
            action('SetExpression('+Librarian.name+',surprised)')
            action('SetDialog("'+Librarian.name+' : What??")')
            action('Wait(2)') 
            action('SetDialog("'+Harry.name+' : I need more information on Palpatine to save our princess.")')
            action('Wait(2)') 
            action('SetDialog("'+Librarian.name+' : Sure General! I have scroll that contains his details")')
            action('Wait(2)') 
            action('HideDialog()')
            action('SetLeft(null)')
            action('SetRight(null)')
            action('DisableIcon("Talk",'+Librarian.name+')')
            action('WalkTo('+Librarian.name+','+Library.name+'.AlchemistTable.Left)')
            action('Pickup('+Librarian.name+',Scroll,'+Library.name+'.AlchemistTable.Left)')
            action('WalkTo('+Librarian.name+','+Harry.name+')')
            action('Give('+Librarian.name+',Scroll,'+Harry.name+')')
            action('AddToList(Scroll,"Scroll - contains information about Palpatine")')
            action('ShowList('+Harry.name+')')
            action('SetCameraFocus('+Harry.name+')')
            action('SetCameraMode(follow)')
            action('EnableInput()')
        
        elif received == 'input Key Inventory':
            action('ShowList('+Harry.name+')')

        # elif received == 'input Pick GoldBag':
            # action('DisableInput()')
            # action('WalkTo('+Harry.name+','+Storage.name+'.Shelf)')
            # action('Pickup('+Harry.name+',GoldBag,'+Storage.name+'.Shelf)')
            # action('AddToList(GoldBag,"Gold coins bag - used to buy weapons from Blacksmith")')
            # action('ShowList('+Harry.name+')')
            # global bagFlag
            # bagFlag=True
            # action('EnableInput()')
            
        # elif received == 'input Pick GoldCup':
            # action('DisableInput()')
            # action('WalkTo('+Harry.name+','+Storage.name+'.Shelf)')
            # action('Pickup('+Harry.name+',GoldCup,'+Storage.name+'.Shelf)')
            # action('AddToList(GoldCup,"Gold Cup - used to buy potions from Alchemist")')
            # action('ShowList('+Harry.name+')')
            # global cupFlag
            # cupFlag=True
            # action('EnableInput()')
            
        elif received == 'input Close List':
            action('HideList()')
            

# while(True):
	# i = input()
	# if i == 'input Selected Start':
		# action('HideMenu()')
		# action('EnableInput()')
		# 
		# Narrate('Welcome to "The Kidnapping in Moore City"')
		# action('Wait(3)')
		# Narrate.Hide_Narration()
		# Great_hall()
		# CourtYard(Harry,Moore_Courtyard)
        
  
# Main Function starts here  
if __name__ == "__main__":
    main()