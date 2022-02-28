from action import action
class Create_Character:
    #Class for creating characters
    def __init__(self, name, body, clothing, hair, expression):
        self.name=name
        action('CreateCharacter('+name+','+body+')')
        action('SetClothing('+name+','+clothing+')')
        action('SetHairStyle('+name+','+hair+')')
        action('SetExpression('+name+','+expression+')')