import game_loop
import player_main_attr as player
import player_main_stats as stats
import additional_functions as extra
import json

# Selected Save Test
selected_save = "testSave"

###This will grab the current room from the save file, possibly the party's variable### 
with open(f'save_files/{selected_save}.json') as saveDataJson:
    saveData = json.load(saveDataJson)
    saveDataJson.close()
currentRoom = saveData["saves"]["currentRoom"]

extra.clear()

run = game_loop.GameLoop(currentRoom)
run.loop()