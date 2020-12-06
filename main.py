import game_loop
import player
# import player_main_stats as stats
import extra_functions as extra
import json
import pygame
import time
import shutil
import sys
import os

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

hide_cursor()

# Selected Save Test
selected_save = "testSave"

###This will grab the current room from the save file, possibly the party's variable### 
with open(f'save_files/{selected_save}.json') as saveDataJson:
    saveData = json.load(saveDataJson)
    saveDataJson.close()
currentRoom = saveData["saves"]["currentRoom"]

columns = shutil.get_terminal_size().columns

extra.clear()
print("\n\n\n\n")
print("Blood Mountain Studios presents:".center(columns))
time.sleep(2)
extra.clear()
print("\n\n\n\n")
print("The Crucible Skull".center(columns))
time.sleep(2.5)
extra.clear()


run = game_loop.GameLoop(currentRoom)

''' Music test '''
# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
# pygame.init() #turn all of pygame on.
# pygame.mixer.music.load('sounds/testmusic.wav')
# pygame.mixer.music.play(-1)

run.loop()