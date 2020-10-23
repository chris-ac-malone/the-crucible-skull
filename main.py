import game_loop
import player_main_attr as player
import player_main_stats as stats
import json

###Testing rooms###
running = True

###This will grab the current room from the save file, possibly the party's variable### 
with open('save_files/defaultSave.json') as saveDataJson:
    saveData = json.load(saveDataJson)
    saveDataJson.close()
currentRoom = saveData["saves"]["currentRoom"]
run = game_loop.GameLoop()
run.loop(currentRoom)