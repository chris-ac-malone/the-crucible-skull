###Player Stats###


class PlayerStats:
    ###Member Variables###
    __strength = 0
    __endurance = 0
    __intelligence = 0
    __charisma = 0
    __speed = 0

    ###Member Methods###
    def getStrength(self):
        return self.__strength
    def setStrength(self, newStrength):
        self.__strength = newStrength

    def getEndurance(self):
        return self.__endurance
    def setEndurance(self, newEndurance):
        self.__endurance = newEndurance

    def getIntelligence(self):
        return self.__intelligence
    def setIntelligence(self, newIntelligence):
        self.__intelligence = newIntelligence

    def getCharisma(self):
        return self.__charisma
    def setCharisma(self, newCharisma):
        self.__charisma = newCharisma

    def getSpeed(self):
        return self.__speed
    def setSpeed(self, newSpeed):
        self.__speed = newSpeed
