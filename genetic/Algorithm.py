from Population import Population
from Individual import Individual
from random import randrange

class Algorithm :
    
    def __init__(self, nbIndividuals, nbGeneration) :
        self._population = None
        self._nbIndividuals = nbIndividuals
        self._nbGeneration = nbGeneration
        
    def getPopulation(self) :
        return self._population
    
    def setPopulation(self, population) :
        self._population = population
        
    def run(self) :
                
        p = Population(self._nbIndividuals)
        p.initialPopulation()
        
        self._population = p.getPopulation()
        generation = 0
        
        while(generation < self._nbGeneration) :
            
            print(generation)
            
            #evaluating the generation 
            self._evaluatePopulation()
            
            #print("evaluation :\n")
            #print(self._population)
            #print("\n")
                        
            #sorting by fitness and selecting the parents 
            #self._sortByIncreasingFitness()
            self._population = self._tournamentSelection(int(len(self._population)/2))
            #self._population = self._tournamentBinarySelection(int(len(self._population)/2))
            #self._population = self._population[:int(len(self._population)/2)]
            
            #print("selecting parents :\n")
            #print(self._population)
            #print("\n")
            
            #breed all the child
            #self._sortByIncreasingFitness()
            self._breedAndMutate()
            self._evaluatePopulation()
            
             
            #print("breeding and mutate :\n")
            #print(self._population)
            #print("\n")

            #selecting the next generation 
            self._population = self._population[:self._nbIndividuals]

            
            #print("selecting next generation to pass :\n")
            #print(self._population)
            #print("\n")
                        
            generation += 1
            print(self._population)
        print("\n")
        return self.correctPlannings()
        
            
    def _tournamentBinarySelection(self, limit) :
        n = len(self._population)
        selected = []
        while(len(selected) < limit) :
            k = randrange(n)
            j = randrange(n)
            if self._population[k].getFitness() >= self._population[j].getFitness() :
                selected.append(self._population[k])
        return selected
    
    def _tournamentSelection(self, limit) :
        self._sortByIncreasingFitness()
        selected = self._population[:limit]
        return selected
        
        
    def _evaluatePopulation(self) :
        for individual in self._population :
            self._maxiMinFitness(individual)
        
    def _maxiMinFitness(self, individual) :
        minimums = []
        for other in self._population :
            distanceDifference = individual.getDistance() - other.getDistance()
            changementDifference = individual.getDistance() - other.getDistance()
            if individual.getId() != other.getId() :
                minimums.append(min(distanceDifference, changementDifference))
        individual.setFitness(1 - max(minimums))
        
    def _sortByIncreasingFitness(self) : 
        for i in range(len(self._population)-1) :
            for j in range(i+1, len(self._population)) :
                indAtI = self._population[i]
                indAtJ = self._population[j]
                if indAtI.getFitness() > indAtJ.getFitness() :
                    self._population[i] = indAtJ
                    self._population[j] = indAtI
    """                
    def _breedAndMutate(self) :
        for i in range(len(self._population)-1) :
            for j in range(i+1, len(self._population)) :
                children = self._tekMiddleCrossing(self._population[i], self._population[j])
                for child in children :
                    self._mutations(child)
                    self._population.append(child)
    """
    
    def _breedAndMutate(self) :
        popLen = len(self._population)
        for i in range (popLen) : 
            rand1, rand2 = randrange(popLen), randrange(popLen)
            parent1, parent2 = self._population[rand1], self._population[rand2]
            children = self._tekMiddleCrossing(parent1, parent2)
            for child in children :
                    self._mutations(child)
                    self._population.append(child)
        
    
    def _mutations(self, individual) :
        #self._changementMutations(individual)
        #self._distanceMutations(individual)
        randomNumber = randrange(6)
        
        if randomNumber == 0 : 
            individual.tekChangementMutation(0, [1, 2])
            
        if randomNumber == 1 : 
            individual.tekChangementMutation(1, [2])

        elif randomNumber == 2 : 
            individual.tekChangementMutation(2, [0, 1])

        elif randomNumber == 3 :
            individual.tekDistanceMutation(0, [1, 2])

        elif randomNumber == 4 :
            individual.tekDistanceMutation(1, [2])

        elif randomNumber == 5 : 
            individual.tekChangementMutation(2, [0, 1])
    
    def _changementMutations(self, individual) :
        individual.tekChangementMutation(0, [1, 2])
        individual.tekChangementMutation(1, [2])
        individual.tekChangementMutation(2, [0, 1])
        
    def _distanceMutations(self, individual) :
        individual.tekDistanceMutation(0, [1, 2])
        individual.tekDistanceMutation(1, [2])
        individual.tekChangementMutation(2, [0, 1])
        

    def _tekMiddleCrossing(self, individual1, individual2) :
        individual1Solution = individual1.getSolution()
        individual2Solution = individual2.getSolution()
        
        firstChildSolution =  [individual1Solution[0], individual1Solution[1], individual2Solution[2]]
        firstChild = Individual()
        firstChild.setSolution(firstChildSolution)
        firstChild.computeIndividualCharacteristics()
        
        secondChildSolution = [individual2Solution[0], individual2Solution[1], individual1Solution[2]]
        secondChild = Individual()
        secondChild.setSolution(secondChildSolution)
        secondChild.computeIndividualCharacteristics()
        
        return (firstChild, secondChild)
    
    def correctPlannings(self) :
        plannings = []
        i = 0
        for plan in self._population :
            if plan.getFitness() == 1 :
                plannings.append(plan)
            i+= 1
        print("\n")
        print("plannings:\n")
        return plannings
            
    
    
    # Mutation : prendre des éléments au hasard au lieu de donner directement un élément 
    
if __name__ == "__main__":

    algo = Algorithm(200, 150)
    print(algo.run())