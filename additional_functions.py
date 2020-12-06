from os import system, name

### Clear Screen ###
running = True
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Prints a list with indices to the left
def print_list(printed_list):
    n = 0
    for (x) in printed_list:
        print(str(n) + ": " + x)
        n += 1

def print_list_party_members(printed_list_party_members):
    n = 0
    for (x) in printed_list_party_members:
        print(str(n) + ": " + x.getName(x))
        n += 1

def print_list_party_reserves(printed_list_party_reserves):
    n = 0
    for (x) in printed_list_party_reserves:
        print(str(n) + ": " + x.getName(x))
        n += 1

def print_help():
    print(f"Move: north, south, east, west, n, s, e, w")
    print(f"Check Party: ")
    print(f"Check Inventory: item list")
    print(f"Save Game: save")
    print(f"Load Game: load")