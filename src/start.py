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

#Create Items for Blacksmith
Sword1=item('Sword1','Sword','Blacksmith.Table.Left')
Sword2=item('Sword2','Sword','Blacksmith.Table.Right')
Sword3=item('Sword3','Sword','Blacksmith.Table.FrontLeft')
Sword4=item('Sword4','Sword','Blacksmith.Table.FrontRight')

#Create Items for Alchemy Shop
SpellBook=item('SpellBook','SpellBook','Alchemy.AlchemistTable.Center')
BluePotion=item('BluePotion','BluePotion','Alchemy.AlchemistTable.Left')
RedPotion=item('RedPotion','RedPotion','Alchemy.AlchemistTable.Right')
RedBook=item('RedBook','RedBook','Alchemy.Bookshelf.Left')
GreenBook=item('GreenBook','GreenBook','Alchemy.Bookshelf.Right')
EvilBook=item('EvilBook','EvilBook','Alchemy.Table.Left')
PurpleBook=item('PurpleBook','PurpleBook','Alchemy.Table.Right')
PurplePotion=item('PurplePotion','PurplePotion','Alchemy.Table.FrontLeft')
GreenPotion=item('GreenPotion','GreenPotion','Alchemy.Table.FrontRight')
Scroll=item('Scroll','Scroll','Alchemy.Table.BackLeft')
OpenScroll=item('OpenScroll','OpenScroll','Alchemy.Table.BackRight')
BlueCloth=item('BlueCloth','BlueCloth','Alchemy.Bar.Behind')
Cup=item('Cup','Cup','Alchemy.Bar.Left')
Bottle=item('Bottle','Bottle','Alchemy.Bar.Center')
Bottle2=item('Bottle2','Bottle','Alchemy.Bar.Right')


#Create Characters
Harry=Create_Character('Harry','B','LightArmour','Long','happy')
Gollum=Create_Character('Gollum','G','Merchant','short_Full','happy')
Stanger=Create_Character('Stranger','H','Peasant','Mage_Full','happy')
Princess_Scarlett=Create_Character('Princess Scarlett','A','Queen','Straight','sad')
Palpatine=Create_Character('Palpatine','F','Bandit','Short_Full','angry')
King_Jonathan=Create_Character('King Jonathan','D','King','Short_Beard','angry')

action('EnableIcon(Book,book,Book,"BlueBook")')
action('SetCameraFocus(Harry)')
action('SetCameraMode(follow)')
action('ShowMenu()')

while(True):
	i = input()
	if i == 'input Selected Start':
		action('HideMenu()')
		action('EnableInput()')
		action('Enter(Harry, Alchemy.Door,true)')

