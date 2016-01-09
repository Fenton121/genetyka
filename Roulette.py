import random
class Roulette():
    def __init__(self,
                 bags,
                 numOfBags):
        self.inputNumOfBags =  numOfBags
        self.bags = bags

    def ResetMembers(self):
        self.roulette = []
        self.rouletteRange = 0
        
    def InitializeRoulette(self):

        numOfBagsForRemove = len(self.bags) - self.inputNumOfBags
        for bagIdx in range(0, 20):
            self.rouletteRange = self.rouletteRange + self.bags[bagIdx].GetValueSum()
            self.roulette.append(self.rouletteRange)
        
    def DrawBagsIdxForRepr(self):
        self.ResetMembers()
        self.InitializeRoulette()
        
        idxsOfBagsForReproduction = []
        bagIdx = 0
        while(len(idxsOfBagsForReproduction) < ( len(self.bags)) ):
            idxOfBagForReprod = self.FindBagFromRange()
            if(idxOfBagForReprod != bagIdx):
                bagIdx = bagIdx + 1;
                idxsOfBagsForReproduction.append(idxOfBagForReprod)
        return idxsOfBagsForReproduction
            
    def FindBagFromRange(self):
        randRange = random.randint(0, self.rouletteRange - 1)
        for bagIdx in range(0, len(self.bags)):
            if(self.roulette[bagIdx] > randRange):
                return bagIdx