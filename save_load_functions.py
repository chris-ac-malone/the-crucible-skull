#import container
#import room
import party_main
import player_main_attr
#import item

import json

# m = open('game_map.json',)
# game_map_data = json.load(m)
# m.close()

s = open('save_files/defaultSave.json',)
saveData = json.load(s)
s.close()

def write_to_json(gameLoop):
    with open('default_save.json', 'w') as save_dump:
        json.dump(gameLoop.game_map_data, save_dump, indent=4)

def loadParty():
    party = party_main.Party()

def loadTheosys():
    theosys = player_main_attr.PlayerAttr

    theosys.setName(theosys, saveData['saves']['characters']['theosys']['attributes']['name'])
    theosys.setLevel(theosys, saveData['saves']['characters']['theosys']['attributes']['level'])
    theosys.setExpCurrent(theosys, saveData['saves']['characters']['theosys']['attributes']['experience_current'])
    theosys.setExpNeed(theosys, saveData['saves']['characters']['theosys']['attributes']['experience_needed'])
    theosys.setHealthCurrent(theosys, saveData['saves']['characters']['theosys']['attributes']['health_current'])
    theosys.setHealthMax(theosys, saveData['saves']['characters']['theosys']['attributes']['health_max'])
    theosys.setManaCurrent(theosys, saveData['saves']['characters']['theosys']['attributes']['mana_current'])
    theosys.setManaMax(theosys, saveData['saves']['characters']['theosys']['attributes']['mana_max'])

    theosys.getPlayerStats(theosys).setStrength(saveData['saves']['characters']['theosys']['stats']['strength'])
    theosys.getPlayerStats(theosys).setEndurance(saveData['saves']['characters']['theosys']['stats']['endurance'])
    theosys.getPlayerStats(theosys).setIntelligence(saveData['saves']['characters']['theosys']['stats']['intelligence'])
    theosys.getPlayerStats(theosys).setCharisma(saveData['saves']['characters']['theosys']['stats']['charisma'])
    theosys.getPlayerStats(theosys).setSpeed(saveData['saves']['characters']['theosys']['stats']['speed'])
    return theosys