from asyncio import wait_for
from Create_Item import item
from create_Character import Create_Character
from create_location import Create_location
from action import action

#Create Places
Castle_Moore=Create_location('Castle_Moore','GreatHall')
City=Create_location('city','City')
Blacksmith=Create_location('Blacksmith','Blacksmith')
Alchemy=Create_location('Alchemy','AlchemyShop')
Spooky_path=Create_location('Spooky_path','SpookyPath')
Dungeon=Create_location('Dungeon','Dungeon')

#Create Items
Book=item('Book','BlueBook','Alchemy.RightBookCase')

#Create Characters
Harry=Create_Character('Harry','B','LightArmour','Long','happy')
Gollum=Create_Character('Gollum','G','Merchant','Musketeer','happy')
Stanger=Create_Character('Stranger','H','Peasant','Mage_Full','happy')
Princess_Scarlett=Create_Character('Princess Scarlett','A','Queen','Straight','sad')
Palpatine=Create_Character('Palpatine','F','Bandit','Short_Full','angry')
King_Jonathan=Create_Character('King Jonathan','D','King','Short_Beard','angry')

action('EnableIcon(Book,book,Book,"BlueBook")')
action('SetCameraFocus(Harry)')
action('SetCameraMode(follow)')
action('EnableInput()')
action('ShowMenu()')
wait_for('input Selected Start')
action('HideMenu()')
action('Enter(Harry, Alchemy.Door,true)')

while(True):
	input()

