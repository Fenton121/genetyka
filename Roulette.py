import random
class Roulette():
    def __init__(self,
                 bags):
        self.bags = bags

    def ResetMembers(self):
        self.roulette = []
        self.rouletteRange = 0
        
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
            
        
    def InitializeRoulette(self):
        numOfBags = len(self.bags)
        for bagIdx in range(0, numOfBags):
            self.rouletteRange = self.rouletteRange + self.bags[bagIdx].GetValue()
            self.roulette.append(self.rouletteRange)
            
    def FindBagFromRange(self):
            randRange = random.randint(0, self.rouletteRange/2 - 1)
            for bagIdx in range(0, len(self.bags)):
                if(self.roulette[bagIdx] > randRange):
                    return bagIdx