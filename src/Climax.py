from location import *
from CreateCharacters import *
from Items import *
from action import action

def placeFarm():
    action('EnableIcon("Enter",exit,'+Farm.name+'.Door,"Enter Dungeon",true)')
    action('Enter('+Harry.name+','+Farm.name+'.Exit,true)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')    

def placeDungeon():
    action('EnableIcon("Talk",talk,'+Palpatine.name+',"Talk to Palpatine")')
    action('EnableIcon("Attack",sword,'+Palpatine.name+',"Attack Palpatine")')
    # action('EnableIcon("Pick",hand,Scroll,"Pick up scroll",true)')
    action('Enter('+Harry.name+','+Dungeon.name+'.Door,true)')
    action('SetCameraFocus('+Harry.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
