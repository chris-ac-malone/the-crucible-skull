import json

class Enemy:
    def __init__(self, enemy_id):
        self.enemy_id = enemy_id

        e = open("enemies.json")
        enemies = json.load(e)
        e.close()

        self.name = enemy_id

        self.hp = enemies["enemies"][f"{self.enemy_id}"]["hp"]
        self.current_hp = enemies["enemies"][f"{self.enemy_id}"]["hp"]
        self.strength = enemies["enemies"][f"{self.enemy_id}"]["strength"]
        self.current_strength = enemies["enemies"][f"{self.enemy_id}"]["strength"]
        self.endurance = enemies["enemies"][f"{self.enemy_id}"]["endurance"]
        self.current_endurance = enemies["enemies"][f"{self.enemy_id}"]["endurance"]
        self.intlligence = enemies["enemies"][f"{self.enemy_id}"]["intelligence"]
        self.current_intlligence = enemies["enemies"][f"{self.enemy_id}"]["intelligence"]
        self.charisma = enemies["enemies"][f"{self.enemy_id}"]["charisma"]
        self.current_charisma = enemies["enemies"][f"{self.enemy_id}"]["charisma"]
        self.speed = enemies["enemies"][f"{self.enemy_id}"]["speed"]
        self.current_speed = enemies["enemies"][f"{self.enemy_id}"]["speed"]

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp
    
    def get_current_hp(self):
        return self.current_hp

        speed_gauge = 0
    
class EnemyParty:
    enemy_list = []

    '''
    testing functions only
    '''
    test_goblin = Enemy("goblin")
    enemy_list.append(test_goblin)
    enemy_list.append(test_goblin)

    def get_enemy_list(self):
        return self.enemy_list