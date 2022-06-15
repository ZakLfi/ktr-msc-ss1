from random import randrange
from gc import collect

class Planning :
    
    def __init__(self) :
        self._planning = [["K", "N", "N", "N"], ["C", "C", "N", "N"], ["N", "N", "K", "K"]]
        self._students = [[100, 1, 40, 40], [50, 50, 1, 35], [40, 1, 100, 100]]
        self._rooms = {"Ha" : 30, "C" : 50, "K" : 130, "Ba" : 40, "P" : 40, "By" : 10, "Tu" : 40, "Hu" : 10}
        self._keys = list(self._rooms.keys())
        
    def getPlanning(self) :
        return self._planning
        
    def _roomsToBeChangedFromPlanningBasis(self) :
        toChange = []
        for i in range(len(self._planning)) :
            for j in range(len(self._planning[i])) :
                if self._planning[i][j] != "K" and self._planning[i][j] != "C" :
                    toChange.append((i, j))
        return toChange
    
    def build(self) :
        toBeChanged = self._roomsToBeChangedFromPlanningBasis()
        for position in toBeChanged :
            finish = True
            concernedTek, slot = position[0], position[1]
            matchingRooms = self._findMatchingRoomsAt(position)
            index = randrange(len(matchingRooms))
            randomRoom = matchingRooms[index]
            while(finish) :
                if (not self._roomAlreadyTakenForIndividualPoint(randomRoom)) and (not self._roomAlreadyInSlots(randomRoom, position)) :
                    self._planning[concernedTek][slot] = randomRoom
                    finish = False
                else :
                    matchingRooms.remove(randomRoom)
                    if len(matchingRooms) == 0 :
                        break
                    index = randrange(len(matchingRooms))
                    randomRoom = matchingRooms[index]
            if len(matchingRooms) == 0 :
                break
        return self
    
    def _findMatchingRoomsAt(self, position) :
        i, j = position[0], position[1]
        capacity = self._students[i][j]
        possibleRooms = []
        for room in self._rooms :
            if self._rooms[room] >= capacity :
                possibleRooms.append(room)
        return possibleRooms

    def _roomAlreadyTakenForIndividualPoint(self, room) :
        return self._planning[0][1] == room or self._planning[1][2] == room or self._planning[2][1] == room
    
    def _roomAlreadyInSlots(self, room, position) :
        concernedTek, slot = position[0], position[1]
        values = []
        allTek = [0, 1, 2]
        for tek in allTek :
            if tek != concernedTek :
                values.append(self._planning[tek][slot] == room)
        return True in values
    

    


