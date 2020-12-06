import party_main
import extra_functions as extra
import save_load_functions as slf
import enemy_party as ep
import json

# Selected Save Test
selected_save = "file1"
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
        extra.clear()

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

                    input("Continue")
                    extra.clear()
                elif(prompt == '1'):
                    n = 0
                    extra.print_list_party_members(self.party.party_members)
                    prompt = input("which party member?")

                    input("Press enter")
                    extra.clear()
                elif(prompt == '2'):
                    n = 0
                    extra.print_list_party_reserves(self.party.party_reserves)

                    input("Press enter")
                    extra.clear()

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
                
            # TODO: Finish the battle loop basics
            def battle_loop(player_party, enemy_party):
                for party_member in player_party.get_party_members():
                    print(f"{party_member.getName()}: {party_member.getHealthCurrent()}/{party_member.getHealthMax()}")
                for enemy in enemy_party.get_enemy_list():
                    print(f"{enemy.get_name()}: {enemy.get_current_hp()}/{enemy.get_hp()}")
                '''
                battle = True
                while(battle == True):
                    loop party members:
                        check speed meter
                        if speed meter > 100 and battle == True:
                            turn
                            speed meter = 0
                        else:
                            increase speed meter by speed
                    loop enemies:
                        check speed meter
                        if speed meter > 100 and battle == True:
                            turn
                            speed meter = 0
                        else:
                            increase speed meter by speed
                
                return player_party?
                '''
                input("Wait")
            def random_battle():
                enemy_party = ep.EnemyParty()
                battle_loop(self.party, enemy_party)
            
            def quit_game():
                quit()


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

                    "items": item_list,

                    "use item": use_item,

                    "give item": debug_give_item,

                    "help": extra.print_help,

                    "battle": random_battle,

                    "quit": quit_game
                }
                func = switch.get(prompt, lambda: "Invalid Input")
                func()
            
            processInput(prompt)