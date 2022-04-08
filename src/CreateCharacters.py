from action import action

def create_characters():
    # Character Harry
    action('CreateCharacter(Harry,B)')
    action('SetClothing(Harry,LightArmour)')
    action('SetHairStyle(Harry,Long)')
    action('SetExpression(Harry,happy)')
    
    # Character Gollum
    action('CreateCharacter(Gollum,G)')
    action('SetClothing(Gollum,Merchant)')
    action('SetHairStyle(Gollum,Short_Full)')
    action('SetExpression(Gollum,happy)')
    
    # Character Stranger
    action('CreateCharacter(Stranger,H)')
    action('SetClothing(Stranger,Peasant)')
    action('SetHairStyle(Stranger,Mage_Full)')
    action('SetExpression(Stranger,happy)')
    
    # Character Princess_Scarlett
    action('CreateCharacter(Princess_Scarlett,A)')
    action('SetClothing(Princess_Scarlett,Queen)')
    action('SetHairStyle(Princess_Scarlett,Straight)')
    action('SetExpression(Princess_Scarlett,sad)')
    
    # Character Palpatine
    action('CreateCharacter(Palpatine,F)')
    action('SetClothing(Palpatine,Bandit)')
    action('SetHairStyle(Palpatine,Short_Full)')
    action('SetExpression(Palpatine,angry)')
    
    # Character King_Jonathan
    action('CreateCharacter(King_Jonathan,D)')
    action('SetClothing(King_Jonathan,King)')
    action('SetHairStyle(King_Jonathan,Short_Beard)')
    action('SetExpression(King_Jonathan,happy)')
    
    # Character GH_guard1
    action('CreateCharacter(guard1,A)')
    action('SetClothing(guard1,HeavyArmour)')
    action('SetHairStyle(guard1,Spiky)')
    action('SetExpression(guard1,neutral)')
    
    # Character GH_guard2
    action('CreateCharacter(guard2,B)')
    action('SetClothing(guard2,HeavyArmour)')
    action('SetHairStyle(guard2,Long)')
    action('SetExpression(guard2,neutral)')
    
    # Character GH_guard3
    action('CreateCharacter(guard3,C)')
    action('SetClothing(guard3,HeavyArmour)')
    action('SetHairStyle(guard3,Spiky)')
    action('SetExpression(guard3,neutral)')
    
    # Character GH_guard4
    action('CreateCharacter(guard4,D)')
    action('SetClothing(guard4,HeavyArmour)')
    action('SetHairStyle(guard4,Short_Full)')
    action('SetExpression(guard4,neutral)')
    
    # Character GH_guard5
    action('CreateCharacter(guard5,E)')
    action('SetClothing(guard5,HeavyArmour)')
    action('SetHairStyle(guard5,Long)')
    action('SetExpression(guard5,neutral)')
    
    # Character GH_guard6
    action('CreateCharacter(guard6,F)')
    action('SetClothing(guard6,HeavyArmour)')
    action('SetHairStyle(guard6,Short_Full)')
    action('SetExpression(guard6,neutral)')
    
    # Character Security1
    action('CreateCharacter(security1,A)')
    action('SetClothing(security1,LightArmour)')
    action('SetHairStyle(security1,Spiky)')
    action('SetExpression(security1,neutral)')
    
    # Character Security2
    action('CreateCharacter(security2,B)')
    action('SetClothing(security2,LightArmour)')
    action('SetHairStyle(security2,Long)')
    action('SetExpression(security2,neutral)')
   
    action('SetPosition(King_Jonathan,Castle_Moore.Throne)')
    action('Sit(King_Jonathan,Castle_Moore.Throne)')
    action('SetPosition(guard1,Castle_Moore.RightBalcony)')
    action('SetPosition(guard2,Castle_Moore.LeftBalcony)')
    action('SetPosition(guard3,Castle_Moore.RightGuard)')
    action('SetPosition(guard4,Castle_Moore.LeftGuard)')
    action('SetPosition(guard5,Castle_Moore.LeftFoyer)')
    action('SetPosition(guard6,Castle_Moore.RightFoyer)')