from action import action

def Create_Item():
    #Create Items for Alchemy shop
    action('CreateItem(SpellBook,SpellBook)')
    action('SetPosition(SpellBook,Alchemy.AlchemistTable.Center)')
    action('CreateItem(BluePotion,BluePotion)')
    action('SetPosition(BluePotion,Alchemy.AlchemistTable.Left)')
    action('CreateItem(RedPotion,RedPotion)')
    action('SetPosition(RedPotion,Alchemy.AlchemistTable.Right)')
    action('CreateItem(RedBook,RedBook)')
    action('SetPosition(RedBook,Alchemy.Bookshelf.Left)')
    action('CreateItem(GreenBook,GreenBook)')
    action('SetPosition(GreenBook,Alchemy.Bookshelf.Right)')
    action('CreateItem(EvilBook,EvilBook)')
    action('SetPosition(EvilBook,Alchemy.Table.Left)')
    action('CreateItem(PurpleBook,PurpleBook)')
    action('SetPosition(PurpleBook,Alchemy.Table.Right)')
    action('CreateItem(PurplePotion,PurplePotion)')
    action('SetPosition(PurplePotion,Alchemy.Table.FrontLeft)')
    action('CreateItem(GreenPotion,GreenPotion)')
    action('SetPosition(GreenPotion,Alchemy.Table.FrontRight)')
    action('CreateItem(Scroll,Scroll)')
    action('SetPosition(Scroll,Alchemy.Table.BackLeft)')
    action('CreateItem(OpenScroll,OpenScroll)')
    action('SetPosition(OpenScroll,Alchemy.Table.BackRight)')
    action('CreateItem(BlueCloth,BlueCloth)')
    action('SetPosition(BlueCloth,Alchemy.Bar.Behind)')
    action('CreateItem(Cup2,Cup)')
    action('SetPosition(Cup2,Alchemy.Bar.Left)')
    action('CreateItem(Bottle,Bottle)')
    action('SetPosition(Bottle,Alchemy.Bar.Center)')
    action('CreateItem(Bottle2,Bottle)')
    action('SetPosition(Bottle2,Alchemy.Bar.Right)')

    #Create Items for Blacksmith
    action('CreateItem(Sword1,Sword)')
    action('SetPosition(Sword1,Blacksmith.Table.Left)')
    action('CreateItem(Sword2,Sword)')
    action('SetPosition(Sword2,Blacksmith.Table.Righ)')
    action('CreateItem(Sword3,Sword)')
    action('SetPosition(Sword3,Blacksmith.Table.FrontLeft)')
    action('CreateItem(Sword4,Sword)')
    action('SetPosition(Sword4,Blacksmith.Table.FrontRight)')

    #Create Items for Library

           
    action('CreateItem(Scroll2,Scroll)')
    action('SetPosition(Scroll2,Library.AlchemistTable.Left)')
    action('CreateItem(EvilBook2,EvilBook)')
    action('SetPosition(EvilBook2,Library.AlchemistTable.Center)')
    action('CreateItem(InkandQuill,InkandQuill)')
    action('SetPosition(InkandQuill,Library.AlchemistTable.Right)')

    #Create Items for Dungeon

    action('CreateItem(ChickenLeg,ChickenLeg)')
    action('SetPosition(ChickenLeg,Dungeon.Table.Left)')
    action('CreateItem(OpenScroll2,OpenScroll)')
    action('SetPosition(OpenScroll2,Dungeon.Table.FrontLeft)')
    action('CreateItem(Drink,Bottle)')
    action('SetPosition(Drink,Dungeon.Table.BackLeft)')
    action('CreateItem(InkandQuill2,InkandQuill)')
    action('SetPosition(InkandQuill2,Dungeon.Table.FrontRight)')
    action('CreateItem(Sword_vill,Sword)')
    action('SetPosition(Sword_vill,Dungeon.Table.BackRight)')
    action('CreateItem(Rags,Rags)')
    action('SetPosition(Rags,Dungeon.Bookshelf.Left)')
    action('CreateItem(Scroll_dung,Scroll)')
    action('SetPosition(Scroll_dung,Dungeon.Bookshelf.Right)')

    # Create Items for Court Yard
    
    action('CreateItem(RedCloth,RedCloth)')
    action('SetPosition(RedCloth,Moore_Courtyard.BigStall.Left)')
    action('CreateItem(PurpleCloth,PurpleCloth)')
    action('SetPosition(PurpleCloth,Moore_Courtyard.BigStall.Right)')
    action('CreateItem(Sword5,Sword)')
    action('SetPosition(Sword5,Moore_Courtyard.RightBench.Left)')
    action('CreateItem(Sword6,Sword)')
    action('SetPosition(Sword6,Moore_Courtyard.LeftBench.Right)')

    # Create Items for Storage
    
    action('CreateItem(Bag,Bag)')
    action('SetPosition(Bag,Storage.Shelf.Left)')
    action('CreateItem(GoldCup,GoldCup)')
    action('SetPosition(Bag,Storage.Shelf.Right)')