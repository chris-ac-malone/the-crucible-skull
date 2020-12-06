import party_main
import additional_functions as extra
import save_load_functions as slf
import json

# Selected Save Test
selected_save = "testSave"
####################################################
# GameLoop is where all of the navigation will take
# place, loading the map data and beginning other
# encounters, and handling loot in conjunction with
# the inventory classes.
####################################################

class GameLoop:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        pass

    __running = True

    s = open(f'save_files/{selected_save}.json',)
    save_data = json.load(s)
    s.close()

    # loadGame() will load all of the save date from the json and create objects
    # for them. 
    def loadGame(self):
        with open(f'save_files/{selected_save}.json') as save_data_json:
            saveData = json.load(save_data_json)
        self.party = party_main.Party()
        self.party.theosys.debugDisplay(self.party.theosys)
        extra.print_list(self.party.theosys_inventory)

    def saveGame(self):
        slf.write_to_json(self)

    # TODO loop() will receive pre-populated objects
    def loop(self):
        self.loadGame()
        while(self.__running == True):
            ###Display Decription of currentRoom###
            print(self.save_data['saves']['rooms'][self.currentRoom]['description'])

            ###This is a prototype of the prompy which will probably be in the world map class###
            prompt = input("> ")
            extra.clear()

            ### define functions: navigation ###

            def go_north():
                if(self.save_data['saves']['rooms'][self.currentRoom]['north']) == ('x'):
                    print("There is nothing to the north")
                elif(self.save_data['saves']['rooms'][self.currentRoom]['north']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    self.currentRoom = self.save_data['saves']['rooms'][self.currentRoom]['north']

            def go_south():
                if(self.save_data['saves']['rooms'][self.currentRoom]['south']) == ('x'):
                    print("There is nothing to the south")
                elif(self.save_data['saves']['rooms'][self.currentRoom]['south']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    self.currentRoom = self.save_data['saves']['rooms'][self.currentRoom]['south']
                return self.currentRoom

            def go_east():
                if(self.save_data['saves']['rooms'][self.currentRoom]['east']) == ('x'):
                    print("There is nothing to the east")
                elif(self.save_data['saves']['rooms'][self.currentRoom]['east']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    self.currentRoom = self.save_data['saves']['rooms'][self.currentRoom]['east']
                return self.currentRoom

            def go_west():
                if(self.save_data['saves']['rooms'][self.currentRoom]['west']) == ('x'):
                    print("There is nothing to the west")
                elif(self.save_data['saves']['rooms'][self.currentRoom]['west']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    self.currentRoom = self.save_data['saves']['rooms'][self.currentRoom]['west']
                return self.currentRoom

            def unlock_test():
                print(self.save_data['saves']['rooms']['test_00']['east'])
                self.save_data['saves']['rooms']['test_00']['east'] = 'test_east'
                print(self.save_data['saves']['rooms']['test_00']['east'])
                return self.currentRoom

            def item_list():
                print("0: Party\n1: Party Member\n2: Reserves")
                prompt = input("Which group? > ")
                path = ""
                if(prompt == '0'):
                    n = 0
                    extra.print_list(self.party.party_inventory)
                elif(prompt == '1'):
                    n = 0
                    extra.print_list_party_members(self.party.party_members)
                    prompt = input("which party member?")
                #for (v) in self.save_data['saves']['characters']['theosys']['inventory']:
                #    if(v != "x"):
                #        print(str(n) + ": " + v)
                #    n += 1
                return n
                #print(self.save_data['saves']['characters']['theosys']['inventory']["0"])

            def use_item():
                # TODO ask which character from party
                n = item_list() - 1
                consumed_item = input("Which item? > ")
                consumed_item = consumed_item.strip()
                if not consumed_item:
                    print("Invalid entry")
                elif(consumed_item.isdigit() == True):
                    if(int(consumed_item) > n) or (int(consumed_item) < 0):
                        print("Invalid entry")
                    else:
                        # TODO Manage item effects, possibly in the additional functions file
                        self.save_data['saves']['characters']['theosys']['inventory'].pop(int(consumed_item))
                else:
                    print("Invalid entry")

            def debug_give_item():
                self.save_data['saves']['characters']['theosys']['inventory'].append("magic amulet")

            def battle_loop():
                pass


            ### Process Input ###

            def processInput(prompt):
                switch = {
                    "north": go_north,
                    "south": go_south,
                    "east": go_east,
                    "west": go_west,
                    "n": go_north,
                    "s": go_south,
                    "e": go_east,
                    "w": go_west,

                    "save": self.saveGame,

                    "unlock": unlock_test,

                    "item list": item_list,

                    "use item": use_item,

                    "give item": debug_give_item,

                    "help": extra.print_help
                }
                func = switch.get(prompt, lambda: "Invalid Input")
                func()
            
            processInput(prompt)