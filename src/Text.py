from action import action
#class for creating dialogs

class Text:
    def __init__(self,Name,dialogue):
        self.Name=Name
        self.dialogue=dialogue
        action('SetDialog('+Name+' : '+dialogue+')')
        action('ShowDialog()')
        action('Wait(3)')
        action('HideDialog()')
