from Create_Item import item
from create_Character import Create_Character
from create_location import Create_location
from greathall import Great_hall
from courtYard import CourtYard
from action import action

 #Create Places
Castle_Moore=Create_location('Castle_Moore','GreatHall')
City=Create_location('city','City')
Blacksmith=Create_location('Blacksmith','Blacksmith')
Alchemy=Create_location('Alchemy','AlchemyShop')
Spooky_path=Create_location('Spooky_path','SpookyPath')
Dungeon=Create_location('Dungeon','Dungeon')
Moore_Courtyard=Create_location('Moore_Courtyard','Courtyard')

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

#Create Items for Dungeon
ChickenLeg=item('ChickenLeg','ChickenLeg','Dungeon.Table.Left')
Bread=item('Bread','Bread','Dungeon.Table.Right')
OpenScroll2=item('OpenScroll2','OpenScroll','Dungeon.Table.FrontLeft')
Drink=item('Drink','Bottle','Dungeon.Table.BackLeft')
InkandQuill=item('InkandQuill','InkandQuill','Dungeon.Table.FrontRight')
Sword_vill=item('Sword_vill','Sword','Dungeon.Table.BackRight')
Rags=item('Rags','Rags','Dungeon.Bookshelf.Left')
Scroll_dung=item('Scroll_dung','Scroll','Dungeon.Bookshelf.Right')

#Create Items for Court Yard
RedCloth=item('RedCloth','RedCloth','Moore_Courtyard.BigStall.Left')
PurpleCloth=item('PurpleCloth','PurpleCloth','Moore_Courtyard.BigStall.Right')
Sword5=item('Sword5','Sword','Moore_Courtyard.RightBench.Left')
Sword6=item('Sword6','Sword','Moore_Courtyard.LeftBench.Right')

#Create Characters
Harry=Create_Character('Harry','B','LightArmour','Long','happy')
Gollum=Create_Character('Gollum','G','Merchant','Short_Full','happy')
Stanger=Create_Character('Stranger','H','Peasant','Mage_Full','happy')
Princess_Scarlett=Create_Character('Princess Scarlett','A','Queen','Straight','sad')
Palpatine=Create_Character('Palpatine','F','Bandit','Short_Full','angry')
King_Jonathan=Create_Character('King Jonathan','D','King','Short_Beard','happy')

action('SetCameraFocus(Harry)')
action('SetCameraMode(follow)')
action('ShowMenu()')

while(True):
	i = input()
	if i == 'input Selected Start':
		action('HideMenu()')
		action('EnableInput()')
		action('FadeOut()')
		Great_hall(King_Jonathan,Harry,Castle_Moore)
		CourtYard(Harry,Moore_Courtyard)


