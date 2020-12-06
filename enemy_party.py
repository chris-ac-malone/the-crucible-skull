import json

class Enemy:
    def __init__(self, enemy_id):
        self.enemy_id = enemy_id

        e = open("enemies.json")
        enemies = json.load(e)
        e.close()

        hp = enemies["enemies"][f"{self.enemy_id}"]["hp"]
        current_hp = enemies["enemies"][f"{self.enemy_id}"]["hp"]
        strength = enemies["enemies"][f"{self.enemy_id}"]["strength"]
        current_strength = enemies["enemies"][f"{self.enemy_id}"]["strength"]
        endurance = enemies["enemies"][f"{self.enemy_id}"]["endurance"]
        current_endurance = enemies["enemies"][f"{self.enemy_id}"]["endurance"]
        intlligence = enemies["enemies"][f"{self.enemy_id}"]["intelligence"]
        current_intlligence = enemies["enemies"][f"{self.enemy_id}"]["intelligence"]
        charisma = enemies["enemies"][f"{self.enemy_id}"]["charisma"]
        current_charisma = enemies["enemies"][f"{self.enemy_id}"]["charisma"]
        speed = enemies["enemies"][f"{self.enemy_id}"]["speed"]
        current_speed = enemies["enemies"][f"{self.enemy_id}"]["speed"]

        speed_gauge = 0
    
class EnemyParty:
    enemy_list = []

    '''
    testing functions only
    '''
    test_goblin = Enemy("goblin")
    enemy_list.append(test_goblin)