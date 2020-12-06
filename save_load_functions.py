#import container
#import room
import party_main
import player_main_attr
#import item

import json

# Selected Save Test
selected_save = "testSave"

# m = open('game_map.json',)
# game_map_data = json.load(m)
# m.close()

s = open(f'save_files/{selected_save}.json',)
saveData = json.load(s)
s.close()

def write_to_json(gameLoop):
    with open('default_save.json', 'w') as save_dump:
        json.dump(gameLoop.game_map_data, save_dump, indent=4)

def loadParty():
    party = party_main.Party()

def load_theosys():
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

def load_sideline_steve():
    sideline_steve = player_main_attr.PlayerAttr

    sideline_steve.setName(sideline_steve, saveData['saves']['characters']['sideline steve']['attributes']['name'])
    sideline_steve.setLevel(sideline_steve, saveData['saves']['characters']['sideline steve']['attributes']['level'])
    sideline_steve.setExpCurrent(sideline_steve, saveData['saves']['characters']['sideline steve']['attributes']['experience_current'])
    sideline_steve.setExpNeed(sideline_steve, saveData['saves']['characters']['sideline steve']['attributes']['experience_needed'])
    sideline_steve.setHealthCurrent(sideline_steve, saveData['saves']['characters']['sideline steve']['attributes']['health_current'])
    sideline_steve.setHealthMax(sideline_steve, saveData['saves']['characters']['sideline steve']['attributes']['health_max'])
    sideline_steve.setManaCurrent(sideline_steve, saveData['saves']['characters']['sideline steve']['attributes']['mana_current'])
    sideline_steve.setManaMax(sideline_steve, saveData['saves']['characters']['sideline steve']['attributes']['mana_max'])

    sideline_steve.getPlayerStats(sideline_steve).setStrength(saveData['saves']['characters']['sideline steve']['stats']['strength'])
    sideline_steve.getPlayerStats(sideline_steve).setEndurance(saveData['saves']['characters']['sideline steve']['stats']['endurance'])
    sideline_steve.getPlayerStats(sideline_steve).setIntelligence(saveData['saves']['characters']['sideline steve']['stats']['intelligence'])
    sideline_steve.getPlayerStats(sideline_steve).setCharisma(saveData['saves']['characters']['sideline steve']['stats']['charisma'])
    sideline_steve.getPlayerStats(sideline_steve).setSpeed(saveData['saves']['characters']['sideline steve']['stats']['speed'])
    return sideline_steve