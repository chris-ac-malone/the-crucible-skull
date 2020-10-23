from os import system, name

### Clear Screen ###
running = True
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
