
roomCode = "a"
class Room(self, roomCode, description, roomAttributes, 
        __north, __south, __east, __west, containers):

    self.roomCode = roomCode
    self.description = description
    self.roomAttributes = roomAttributes
    self.__north = __north
    self.__south = __south
    self.__east = __east
    self.__west = __west
    self.containers = containers
    #self.hostileEncounters = hostileEncounters
    #self.friendlyEncounters = friendlyEncounters