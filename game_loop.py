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

    def loadGame():
        pass
        # TODO fill out load data function
        # currentRoom
        # all characters, all attributes, all stats
        # all event flags

    def saveGame():
        pass
        # TODO fill out save game function, write to json

    # TODO loop() will receive pre-populated objects
    def loop(self, currentRoom):
        while(self.__running == True):
        #Get room description
            with open('game_map.json') as game_map_data_json:
                game_map_data = json.load(game_map_data_json)

            ###Display Decription of currentRoom###
            print(game_map_data['rooms'][currentRoom][0]['description'])

            ###This is a prototype of the prompy which will probably be in the world map class###
            prompt = input("> ")
            if(prompt == "north"):
                if(game_map_data['rooms'][currentRoom][0]['north']) == ('x'):
                    print("There is nothing to the north")
                else:
                    currentRoom = game_map_data['rooms'][currentRoom][0]['north']
            elif(prompt == "south"):
                if(game_map_data['rooms'][currentRoom][0]['south']) == ('x'):
                    print("There is nothing to the south")
                else:
                    currentRoom = game_map_data['rooms'][currentRoom][0]['south']
            elif(prompt == "east"):
                if(game_map_data['rooms'][currentRoom][0]['east']) == ('x'):
                    print("There is nothing to the east")
                else:
                    currentRoom = game_map_data['rooms'][currentRoom][0]['east']
            elif(prompt == "west"):
                if(game_map_data['rooms'][currentRoom][0]['west']) == ('x'):
                    print("There is nothing to the west")
                else:
                    currentRoom = game_map_data['rooms'][currentRoom][0]['west']
