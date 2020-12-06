###Player Stats###

class PlayerStats:
    ###Member Variables###
    # TODO: I think I ned to add current values for ach of these for status effects
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


class PlayerAttr:
    ###Member Variables###
    __name = "Default"
    __level = 0
    __expCurrent = 0
    __expNeed = 0
    __healthMax = 0
    healthCurrent = 0
    __manaMax = 0
    manaCurent = 0
    __playerStats = PlayerStats()

    ###Methods###
    def getName(self):
        return self.__name
    def setName(self, newName):
        self.__name = newName

    def getLevel(self):
        return self.__level
    def setLevel(self, newLevel):
        self.__level = newLevel

    def getExpCurrent(self):
        return self.__expCurrent
    def setExpCurrent(self, newExpCurrent):
        self.__expCurrent = newExpCurrent
    def getExpNeed(self):
        return self.__expNeed
    def setExpNeed(self, newExpNeed):
        self.__expNeed = newExpNeed

    def getHealthCurrent(self):
        return self.healthCurrent
    def setHealthCurrent(self, newHealthCurrent):
        self.healthCurrent = newHealthCurrent
    def getHealthMax(self):
        return self.__healthMax
    def setHealthMax(self, newHealthMax):
        self.__healthMax = newHealthMax

    def getManaCurrent(self):
        return self.manaCurent
    def setManaCurrent(self, newManaCurrent):
        self.manaCurrent = newManaCurrent
    def getManaMax(self):
        return self.__manaMax
    def setManaMax(self, newManaMax):
        self.__manaMax = newManaMax

    def getPlayerStats(self):
        return self.__playerStats
    # def setPlayerStats(self...)

    def debugDisplay(self):
        print("Name: " + self.getName())
        print("Level: " + str(self.getLevel()))
        print("Exp: " + str(self.getExpCurrent()) + "/" + str(self.getExpNeed()))
        print("HP: " + str(self.getHealthCurrent()) + "/" + str(self.getHealthMax()))
        print("MP: " + str(self.getManaCurrent()) + "/" + str(self.getManaMax()) + "\n")

        print("Str: " + str(self.getPlayerStats().getStrength()))
        print("End: " + str(self.getPlayerStats().getEndurance()))
        print("Int: " + str(self.getPlayerStats().getIntelligence()))
        print("Chr: " + str(self.getPlayerStats().getCharisma()))
        print("Spd: " + str(self.getPlayerStats().getSpeed()))


