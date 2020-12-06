import game_loop
import player
# import player_main_stats as stats
import additional_functions as extra
import json
import pygame

# Selected Save Test
selected_save = "testSave"

###This will grab the current room from the save file, possibly the party's variable### 
with open(f'save_files/{selected_save}.json') as saveDataJson:
    saveData = json.load(saveDataJson)
    saveDataJson.close()
currentRoom = saveData["saves"]["currentRoom"]

extra.clear()


run = game_loop.GameLoop(currentRoom)

''' Music test '''
# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
# pygame.init() #turn all of pygame on.
# pygame.mixer.music.load('sounds/testmusic.wav')
# pygame.mixer.music.play(-1)

run.loop()