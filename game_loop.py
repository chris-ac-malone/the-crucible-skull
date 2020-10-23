import party_main as party
import json

####################################################
# GameLoop is where all of the navigation will take
# place, loading the map data and beginning other
# encounters, and handling loot in conjunction with
# the inventory classes.
####################################################

class GameLoop:
    def __init__(self):
        # TODO Might load the latest save file here
        pass

    __running = True

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
    def loop(self, currentRoom):
        ### TODO I think loadGame() will go here, before the loop, so
        ### we don't have to pass every single class as a parameter
        ### of the loop function, but they're all here. 
        while(self.__running == True):
        #Get room description
            with open('game_map.json') as game_map_data_json:
                game_map_data = json.load(game_map_data_json)
                game_map_data_json.close()
            ###Display Decription of currentRoom###
            print(game_map_data['rooms'][currentRoom]['description'])

            ###This is a prototype of the prompy which will probably be in the world map class###
            prompt = input("> ")
#            if(prompt == "north"):
#                if(game_map_data['rooms'][currentRoom]['north']) == ('x'):
#                    print("There is nothing to the north")
#                elif(game_map_data['rooms'][currentRoom]['north']) == ('l'):
#                    print("You cannot currently reach this area")
#                else:
#                    currentRoom = game_map_data['rooms'][currentRoom]['north']
#            elif(prompt == "south"):
#                if(game_map_data['rooms'][currentRoom]['south']) == ('x'):
#                    print("There is nothing to the south")
#                elif(game_map_data['rooms'][currentRoom]['south']) == ('l'):
#                    print("You cannot currently reach this area")
#                else:
#                    currentRoom = game_map_data['rooms'][currentRoom]['south']
#            elif(prompt == "east"):
#                if(game_map_data['rooms'][currentRoom]['east']) == ('x'):
#                    print("There is nothing to the east")
#                elif(game_map_data['rooms'][currentRoom]['east']) == ('l'):
#                    print("You cannot currently reach this area")
#                else:
#                    currentRoom = game_map_data['rooms'][currentRoom]['east']
#            elif(prompt == "west"):
#                if(game_map_data['rooms'][currentRoom]['west']) == ('x'):
#                    print("There is nothing to the west")
#                elif(game_map_data['rooms'][currentRoom]['west']) == ('l'):
#                    print("You cannot currently reach this area")
#                else:
#                    currentRoom = game_map_data['rooms'][currentRoom]['west']
#            elif(prompt == "unlock"):
#                pass


            #################################################
            ########### Testing switch statement ############
            #################################################
            def go_north(currentRoom):
                if(game_map_data['rooms'][currentRoom]['north']) == ('x'):
                    print("There is nothing to the north")
                elif(game_map_data['rooms'][currentRoom]['north']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    currentRoom = game_map_data['rooms'][currentRoom]['north']
                return currentRoom

            def go_south(currentRoom):
                if(game_map_data['rooms'][currentRoom]['south']) == ('x'):
                    print("There is nothing to the south")
                elif(game_map_data['rooms'][currentRoom]['south']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    currentRoom = game_map_data['rooms'][currentRoom]['south']
                return currentRoom

            def go_east(currentRoom):
                if(game_map_data['rooms'][currentRoom]['east']) == ('x'):
                    print("There is nothing to the east")
                elif(game_map_data['rooms'][currentRoom]['east']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    currentRoom = game_map_data['rooms'][currentRoom]['east']
                return currentRoom

            def go_west(currentRoom):
                if(game_map_data['rooms'][currentRoom]['west']) == ('x'):
                    print("There is nothing to the west")
                elif(game_map_data['rooms'][currentRoom]['west']) == ('l'):
                    print("You cannot currently reach this area")
                else:
                    currentRoom = game_map_data['rooms'][currentRoom]['west']
                return currentRoom




            def processInput(prompt, currentRoom):
                switch = {
                    "north": go_north,
                    "south": go_south,
                    "east": go_east,
                    "west": go_west
                }
                func = switch.get(prompt, lambda: "Invalid Input")
                currentRoom = func(currentRoom)
                return currentRoom
            
            currentRoom = processInput(prompt, currentRoom)