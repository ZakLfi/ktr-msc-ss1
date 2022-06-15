from Planning import Planning
from random import randrange, shuffle
from uuid import uuid1

class Individual :
    
    def __init__(self) :
        self._id = uuid1()
        self._solution = Planning().build().getPlanning()
        self._changement = 0
        self._distance = 0
        self._fitness = 0
        self._rooms = {"Ha" : 30, "C" : 50, "K" : 130, "Ba" : 40, "P" : 40, "By" : 10, "Tu" : 40, "Hu" : 10}
        self._students = [[100, 1, 40, 40], [50, 50, 1, 35], [40, 1, 100, 100]]
        self._distances = {
                            "Ha": {"Ha" : 0, "C" : 2, "K" : 2, "Ba" : 1, "P" : 2, "By" : 3, "Tu" : 4, "Hu" : 5}, 
                            "C" : {"Ha" : 2, "C" : 0, "K" : 1, "Ba" : 1, "P" : 4, "By" : 4, "Tu" : 5, "Hu" : 2},
                            "K" : {"Ha" : 2, "C" : 1, "K" : 0, "Ba" : 0, "P" : 1, "By" : 1, "Tu" : 1, "Hu" : 2},
                            "Ba": {"Ha" : 1, "C" : 1, "K" : 0, "Ba" : 0, "P" : 2, "By" : 3, "Tu" : 4, "Hu" : 5},
                            "P" : {"Ha" : 2, "C" : 4, "K" : 1, "Ba" : 2, "P" : 0, "By" : 0, "Tu" : 1, "Hu" : 3},
                            "By": {"Ha" : 3, "C" : 4, "K" : 1, "Ba" : 3, "P" : 0, "By" : 0, "Tu" : 1, "Hu" : 2},
                            "Tu": {"Ha" : 4, "C" : 5, "K" : 1, "Ba" : 4, "P" : 1, "By" : 1, "Tu" : 0, "Hu" : 1},
                            "Hu": {"Ha" : 5, "C" : 2, "K" : 2, "Ba" : 5, "P" : 3, "By" : 2, "Tu" : 1, "Hu" : 0}
                          }
        
    def getId(self) :
        return self._id
    
    def getSolution(self) :
        return self._solution
    
    def setSolution(self, solution) :
        self._solution = solution
        
    def getChanged(self) :
        return self._changed

    def setChanged(self, changed) :
        self._changement = changed
        
    def getDistance(self) :
        return self._distance

    def setDistance(self, distance) :
        self._distance = distance
        
    def getFitness(self) :
        return self._fitness

    def setFitness(self, fitness) :
        self._fitness = fitness
    
    def computeIndividualCharacteristics(self) :
        self._computeChangements()
        self._computeDistance()
        return self

    def _computeChangements(self) : 
        variation = 0
        for tek in self._solution :
            for i in range(len(tek)-1) :
                if tek[i] != tek[i+1] : variation += 1
        self._changement = variation
        
    def _computeDistance(self) :
        distance  = 0
        for tek in self._solution :
            for i in range(len(tek)-1) :
                distance += self._distanceBetween(tek[i], tek[i+1])
        self._distance = distance
    
    def _distanceBetween(self, room1, room2) :
        return self._distances[room1][room2]

    def _distanceBetweenAt(self, indexRoom1, indexRoom2) :
        keys = list(self._distances.keys())
        concernedKey = keys[indexRoom1]
        return list((self._distances[concernedKey]).values())[indexRoom2]
    
    def tekChangementMutation(self, tek, slots) :
        nbSlots = len(slots)
        randomSlot = slots[randrange(nbSlots)]
        
        currentRoom = self._solution[tek][randomSlot]
        nextRoom = self._solution[tek][randomSlot + 1]
        
        randomNumber = randrange(2)
        
        if currentRoom != nextRoom :
            if (not self._roomAlreadyInSlots(currentRoom, (tek, randomSlot+1))) and self._rooms[currentRoom] >= self._students[tek][randomSlot+1] and randomNumber == 0:
                self._solution[tek][randomSlot + 1] = currentRoom
            elif (not self._roomAlreadyInSlots(nextRoom, (tek, randomSlot))) and self._rooms[nextRoom] >= self._students[tek][randomSlot] and randomNumber == 1:
                self._solution[tek][randomSlot] = nextRoom
                
    def tekDistanceMutation(self, tek, slots) :
        nbSlots = len(slots)
        randomSlot = slots[randrange(nbSlots)]
        
        currentRoom = self._solution[tek][randomSlot]
        nextRoom = self._solution[tek][randomSlot+1]
        
        sameCapacityRooms = self._roomsWithSameCapacity(nextRoom)
        #sortedRooms = self._sortRoomByDistance(currentRoom, sameCapacityRooms)
        
        rdNumber = randrange(len(sameCapacityRooms))
        #room = sortedRooms[i]
        room = sameCapacityRooms[rdNumber]
        dist = self._distanceBetween(currentRoom, nextRoom)
        
        shuffle(sameCapacityRooms)
        
        for room in sameCapacityRooms :
            #dist2 = self._distanceBetween(room, currentRoom)
            if (not self._roomAlreadyTakenForIndividualPoint(room)) and (not self._roomAlreadyInSlots(room, (tek, randomSlot+1))) :
                self._solution[tek][randomSlot+1] = room;
                break;
            
    def _roomsWithSameCapacity(self, room) :
        sameCapacityRooms = []
        for other in self._rooms :
            if other != room and self._rooms[other] >= self._rooms[room]:
                sameCapacityRooms.append(other)
        return sameCapacityRooms
    
    def _sortRoomByDistance(self, room, roomList) : # a changer car tri selon fitness  
        copy = roomList 
        for i in range(len(copy)-1) :
            for j in range(i+1, len(copy)) :
                indAtI = copy[i]
                indAtJ = copy[j]
                if self._distanceBetween(room, indAtI) < self._distanceBetween(room, indAtJ) :
                    copy[i] = indAtJ
                    copy[j] = indAtI
        return copy
            
    def _roomAlreadyTakenForIndividualPoint(self, room) :
        return self._solution[0][1] == room or self._solution[1][2] == room or self._solution[2][1] == room
    
    def _roomAlreadyInSlots(self, room, position) :
        concernedTek, slot = position[0], position[1]
        values = []
        allTek = [0, 1, 2]
        for tek in allTek :
            if tek != concernedTek :
                values.append(self._solution[tek][slot] == room)
        return True in values

    def __str__(self) :
        return "solution :" + str(self._solution) + " changement : " + str(self._changement) + " distance : " + str(self._distance) + " fitness : " + str(self._fitness)
    
    def __repr__(self) :
        return "solution :" + str(self._solution) + " changement : " + str(self._changement) + " distance : " + str(self._distance) + " fitness : " + str(self._fitness) + "\n"
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._solution == other._solution 
        else:
            return False
        
    def __ne__(self, other) :
        return not self.__eq__(other)