import json
import player_main_attr
import save_load_functions as slf
####################################################
# Party is where the party members, individual
# inventory, and party inventory will be stored. 
# It interacts closely with the GameLoop to make
# any changes to party members stats or inventories.
####################################################

class Party:
    def __init__(self):
        pass

    party_members = []

    f = open('save_files/defaultSave.json',)
    save_data = json.load(f)
    f.close()

    theosys = slf.loadTheosys()

    for (x) in save_data['saves']['party']['current']:
        if(x == 'theosys'):
            party_members.append(theosys)
            party_members.append(theosys)

    # TODO Party members will be populated with PlayerAttr objects
    # by iterating through the corresponding save data.
    # I'm hoping I can dynmically create party members for in-game
    # additions. reserves will also be populated with objects. 
    reserve_party_members = save_data['saves']['party']['reserves']

    party_inventory = save_data['saves']['party']['inventory']
    theosys_inventory = save_data['saves']['characters']['theosys']['inventory']