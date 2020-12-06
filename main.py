import game_loop
import extra_functions as extra
import json
import pygame
import time
import shutil
import cursor
from simple_term_menu import TerminalMenu

# Selected Save Test
selected_save = "file1"

# TODO: Remove this, it will be useless when the save file is passed instead. 
def set_current_room():
    with open(f'save_files/{selected_save}.json') as saveDataJson:
        saveData = json.load(saveDataJson)
        saveDataJson.close()
        current_room = saveData["saves"]["currentRoom"]
        return current_room

# Displays the opening credits of the game. Hides the cursor during the scene. 
def introduction():
    cursor.hide()
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    middle = int(lines/2-1)

    extra.clear()
    print("\n" * middle)
    print("Blood Mountain Studios presents:".center(columns))
    time.sleep(2.5)

    extra.clear()
    print("\n" * middle)
    print("The Crucible Skull".center(columns))
    time.sleep(2.5)

    extra.clear()
    cursor.show()

def select_file():
    file_select_menu = TerminalMenu(["[1] File 1","[2] File 2","[3] File 3",
    "[4] File 4","[5] File 5","[6] File 6","[7] File 7","[8] File 8","[9] File 9","[a] File 10",
    "[b] File 11","[c] File 12","[d] File 13","[e] File 14","[f] File 15","[g] File 16"])
    result = file_select_menu.show()
    selected_save = f"file{result+1}.json"
    
    return selected_save

def start_new_game():
    pass

# Creates and displays the title screen where the player chooses a file
def display_title_screen():
    terminal_menu = TerminalMenu(["[1] New Game","[2] Load Game","[3] Quit"])
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        start_new_game()
    elif menu_entry_index == 1:
        select_file()
    elif menu_entry_index == 2:
        quit()


''' Music test '''
# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
# pygame.init() #turn all of pygame on.
# pygame.mixer.music.load('sounds/testmusic.wav')
# pygame.mixer.music.play(-1)

# Runs introduction and file select scene, runs the game loop
# introduction()
# display_title_screen()
run = game_loop.GameLoop(set_current_room())
run.loop()