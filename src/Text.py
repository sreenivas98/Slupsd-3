from action import action

# Modified code for text.py
class Text:
    def setDialog(Name,dialogue):
        action('SetDialog('+Name+' : '+dialogue+')')
        
    def setDialog2(msg):
        action('SetDialog('+msg+')')
        
    def showDialog():
        action('ShowDialog()')
    
    def hideDialog():
        action('HideDialog()')
