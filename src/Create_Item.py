from action import action
#class item used for creating and setting position of an item
class item:
    def __init__(self,item_name,item,position):
        self.item_name=item_name
        action('CreateItem('+item_name+','+item+')')   
        action('SetPosition('+item_name+','+position+')')
