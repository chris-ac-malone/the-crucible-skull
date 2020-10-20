class PlayerAttr:
    ###Member Variables###
    __name = "Theosys"
    __level = 0
    __expCurrent = 0
    __expNeed = 0
    __healthMax = 0
    healthCurrent = 0
    __manaMax = 0
    manaCurent = 0

    ###Methods###
    def getName():
        return __name
    def setName(newName):
        __name = newName

    def getLevel():
        return __level
    def setLevel(newLevel):
        __level = newLevel

    def getExpCurrent():
        return __expCurrent
    def setExpCurrent(newExpCurrent):
        __expCurrent = newExpCurrent
    def getExpNeed():
        return __expNeed
    def setExpNeed(newExpNeed):
        __expNeed = newExpNeed

    def getHealthCurrent():
        return healthCurrent
    def setHealthCurrent(newHealthCurrent):
        healthCurrent = newHealthCurrent
    def getHealthMax():
        return __healthMax
    def setHealthMax(newHealthMax):
        __healthMax = newHealthMax

    def getManaCurrent():
        return manaCurent
    def setManaCurrent(newManaCurrent):
        manaCurrent = newManaCurrent
    def getManaMax():
        return __manaMax
    def setManaMax(newManaMax):
        __manaMax = newManaMax

