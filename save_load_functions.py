import party_main
import player
import json

# Selected Save Test
selected_save = "file1"

# Open the save file and keep it in the variable 'saveData'
s = open(f'save_files/{selected_save}.json',)
saveData = json.load(s)
s.close()

# Writes the data to the save file
def write_to_json(gameLoop):
    with open('default_save.json', 'w') as save_dump:
        json.dump(gameLoop.game_map_data, save_dump, indent=4)

# Loads the party, eg. list of party in each group
def loadParty():
    party = party_main.Party()

# Loads each of the party members
def load_theosys():
    theosys = player.PlayerAttr()

    theosys.setName(saveData['saves']['characters']['theosys']['attributes']['name'])
    theosys.setLevel(saveData['saves']['characters']['theosys']['attributes']['level'])
    theosys.setExpCurrent(saveData['saves']['characters']['theosys']['attributes']['experience_current'])
    theosys.setExpNeed(saveData['saves']['characters']['theosys']['attributes']['experience_needed'])
    theosys.setHealthCurrent(saveData['saves']['characters']['theosys']['attributes']['health_current'])
    theosys.setHealthMax(saveData['saves']['characters']['theosys']['attributes']['health_max'])
    theosys.setManaCurrent(saveData['saves']['characters']['theosys']['attributes']['mana_current'])
    theosys.setManaMax(saveData['saves']['characters']['theosys']['attributes']['mana_max'])

    theosys.getPlayerStats().setStrength(saveData['saves']['characters']['theosys']['stats']['strength'])
    theosys.getPlayerStats().setEndurance(saveData['saves']['characters']['theosys']['stats']['endurance'])
    theosys.getPlayerStats().setIntelligence(saveData['saves']['characters']['theosys']['stats']['intelligence'])
    theosys.getPlayerStats().setCharisma(saveData['saves']['characters']['theosys']['stats']['charisma'])
    theosys.getPlayerStats().setSpeed(saveData['saves']['characters']['theosys']['stats']['speed'])
    return theosys

def load_sideline_steve():
    sideline_steve = player.PlayerAttr()

    sideline_steve.setName(saveData['saves']['characters']['sideline steve']['attributes']['name'])
    sideline_steve.setLevel(saveData['saves']['characters']['sideline steve']['attributes']['level'])
    sideline_steve.setExpCurrent(saveData['saves']['characters']['sideline steve']['attributes']['experience_current'])
    sideline_steve.setExpNeed(saveData['saves']['characters']['sideline steve']['attributes']['experience_needed'])
    sideline_steve.setHealthCurrent(saveData['saves']['characters']['sideline steve']['attributes']['health_current'])
    sideline_steve.setHealthMax(saveData['saves']['characters']['sideline steve']['attributes']['health_max'])
    sideline_steve.setManaCurrent(saveData['saves']['characters']['sideline steve']['attributes']['mana_current'])
    sideline_steve.setManaMax(saveData['saves']['characters']['sideline steve']['attributes']['mana_max'])

    sideline_steve.getPlayerStats().setStrength(saveData['saves']['characters']['sideline steve']['stats']['strength'])
    sideline_steve.getPlayerStats().setEndurance(saveData['saves']['characters']['sideline steve']['stats']['endurance'])
    sideline_steve.getPlayerStats().setIntelligence(saveData['saves']['characters']['sideline steve']['stats']['intelligence'])
    sideline_steve.getPlayerStats().setCharisma(saveData['saves']['characters']['sideline steve']['stats']['charisma'])
    sideline_steve.getPlayerStats().setSpeed(saveData['saves']['characters']['sideline steve']['stats']['speed'])
    return sideline_steve