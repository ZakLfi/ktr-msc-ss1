from Individual import Individual

class Population :
    
    def __init__(self, nbIndividuals) :
        self._nbIndividuals = nbIndividuals
        self._population = []
        self._lastId = nbIndividuals - 1
            
    def initialPopulation(self) :
        for i in range(self._nbIndividuals) :
            individual = Individual().computeIndividualCharacteristics()
            if not self.contains(individual, self._population) :
                self._population.append(individual)
        
    def contains(self, individual, individuals) :
        contains = False
        for ind in individuals :
            if ind == individual :
                contains = True
                break
        return contains 
            
        
    def getNbIndividuals(self) :
        return self._nbIndividuals
    
    def getPopulation(self) :
        return self._population 
    
    def setPopulation(self, population) :
        self._population = population
    
    def __str__(self) :
        return "population : " + str(self._population)
            

if __name__ == "__main__":
    
    population = Population(200)
    population.initialPopulation()
    print(population.getPopulation())