import player_main_attr as player
import player_main_stats as stats
import json

theosis = player.PlayerAttr("Theosys", 0)


###Testing getters and setters###
#print(theosis.getName())
#theosis.setName("Testing")
#print(theosis.getName())

###Testing Getters and Setters for player stats###
#print(theosis.getPlayerStats().getStrength())

###Testing rooms###
running = True

###This will grab the current room from the save file, possibly the party's variable### 
currentRoom = "test_00"

while(running == True):
    #Get room description
    with open('game_map.json') as game_map_data_json:
        game_map_data = json.load(game_map_data_json)
        #currentRoom = "test_00"

        ###Display Decription of currentRoom###
        print(game_map_data['rooms'][currentRoom][0]['description'])

        ###This is a prototype of the prompy which will probably be in the world map class###
        prompt = input("> ")
        if(prompt == "north"):
            if(game_map_data['rooms'][currentRoom][0]['north']) == ('x'):
                print("There is nothing to the north")
            else:
                currentRoom = game_map_data['rooms'][currentRoom][0]['north']
        if(prompt == "south"):
            if(game_map_data['rooms'][currentRoom][0]['south']) == ('x'):
                print("There is nothing to the south")
            else:
                currentRoom = game_map_data['rooms'][currentRoom][0]['south']
        if(prompt == "east"):
            if(game_map_data['rooms'][currentRoom][0]['east']) == ('x'):
                print("There is nothing to the east")
            else:
                currentRoom = game_map_data['rooms'][currentRoom][0]['east']
        if(prompt == "west"):
            if(game_map_data['rooms'][currentRoom][0]['west']) == ('x'):
                print("There is nothing to the west")
            else:
                currentRoom = game_map_data['rooms'][currentRoom][0]['west']