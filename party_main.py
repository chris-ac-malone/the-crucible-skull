import json
import player
import save_load_functions as slf

# Selected Save Test
selected_save = "file1"

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
    party_reserves = []

    f = open(f'save_files/{selected_save}.json',)
    save_data = json.load(f)
    f.close()

    theosys = slf.load_theosys()
    sideline_steve = slf.load_sideline_steve()

    for (x) in save_data['saves']['party']['current']:
        if(x == 'theosys'):
            party_members.append(theosys)
        elif(x == 'sideline steve'):
            party_members.append(sideline_steve)
        else:
            pass

    for (x) in save_data['saves']['party']['reserves']:
        if(x == 'theosys'):
            party_reserves.append(theosys)
        elif(x == 'sideline steve'):
            party_reserves.append(sideline_steve)
        else:
            pass

    def get_party_members(self):
        return self.party_members

    party_inventory = save_data['saves']['party']['inventory']
    theosys_inventory = save_data['saves']['characters']['theosys']['inventory']