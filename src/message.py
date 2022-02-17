from action import action

class Message:
    def __init__(self,Name,dialogue):
        self.Name=Name
        self.dialogue=dialogue
        action('SetDialog('+Name+':'+dialogue+')')
        action('ShowDialog()')
        action('Wait(5)')
        action('HideDialog()')
