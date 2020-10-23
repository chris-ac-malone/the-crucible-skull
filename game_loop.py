import party_main as party
import additional_functions as extra
import json

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

    with open('game_map.json') as game_map_data_json:
        game_map_data = json.load(game_map_data_json)
        game_map_data_json.close()


    f = open('game_map.json',)
    game_map_data = json.load(f)
    f.close()

    # loadGame() will load all of the save date from the json and create objects
    # for them. 
    def loadGame():
        with open('defaultSave.json') as save_data_json:
            saveData = json.load(save_data_json)
        # TODO fill out load data function
        # currentRoom
        # all characters, all attributes, all stats
        # all event flags

    def saveGame():
        pass
        # TODO fill out save game function, write to json

    # TODO loop() will receive pre-populated objects
    def loop(self):
        ### TODO I think loadGame() will go here, before the loop, so
        ### we don't have to pass every single class as a parameter
        ### of the loop function, but they're all here. 
        while(self.__running == True):
        #Get room description
            #with open('game_map.json') as game_map_data_json:
            #    game_map_data = json.load(game_map_data_json)
            #    game_map_data_json.close()
            ###Display Decription of currentRoom###
            print(self.game_map_data['rooms'][self.currentRoom]['description'])

            ###This is a prototype of the prompy which will probably be in the world map class###
            prompt = input("> ")
            extra.clear()

            ### define functions: navigation ###

            def go_north():
                if(self.game_map_data['rooms'][self.currentRoom]['north']) == ('x'):
                    print("There is nothing to the north")
                elif(self.game_map_data['rooms'][self.currentRoom]['north']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    self.currentRoom = self.game_map_data['rooms'][self.currentRoom]['north']

            def go_south():
                if(self.game_map_data['rooms'][self.currentRoom]['south']) == ('x'):
                    print("There is nothing to the south")
                elif(self.game_map_data['rooms'][self.currentRoom]['south']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    self.currentRoom = self.game_map_data['rooms'][self.currentRoom]['south']
                return self.currentRoom

            def go_east():
                if(self.game_map_data['rooms'][self.currentRoom]['east']) == ('x'):
                    print("There is nothing to the east")
                elif(self.game_map_data['rooms'][self.currentRoom]['east']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    self.currentRoom = self.game_map_data['rooms'][self.currentRoom]['east']
                return self.currentRoom

            def go_west():
                if(self.game_map_data['rooms'][self.currentRoom]['west']) == ('x'):
                    print("There is nothing to the west")
                elif(self.game_map_data['rooms'][self.currentRoom]['west']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    self.currentRoom = self.game_map_data['rooms'][self.currentRoom]['west']
                return self.currentRoom

            def unlock_test():
                print(self.game_map_data['rooms']['test_00']['east'])
                self.game_map_data['rooms']['test_00']['east'] = 'test_east'
                print(self.game_map_data['rooms']['test_00']['east'])
                return self.currentRoom

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

                    "unlock": unlock_test
                }
                func = switch.get(prompt, lambda: "Invalid Input")
                func()
            
            processInput(prompt)