from action import action

class Narrate:
    def __init__(self,Message):
        self.Message=Message
        action('SetNarration('+Message+')')
        action('ShowNarration()')

    def Hide_Narration():
        action('HideNarration()')