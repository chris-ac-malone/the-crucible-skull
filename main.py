import game_loop
import player_main_attr as player
import player_main_stats as stats
import additional_functions as extra
import json

###This will grab the current room from the save file, possibly the party's variable### 
with open('save_files/defaultSave.json') as saveDataJson:
    saveData = json.load(saveDataJson)
    saveDataJson.close()
currentRoom = saveData["saves"]["currentRoom"]

extra.clear()

run = game_loop.GameLoop(currentRoom)
run.loop()