import random
class Roulette():
    def __init__(self,
                 bags):
        self.bags = bags
        self.roulette = []
        self.rouletteRange = 0
        self.InitializeRoulette()
        
    def InitializeRoulette(self):
        numOfBags = len(self.bags)
        for bagIdx in range(0, numOfBags):
            self.rouletteRange = self.rouletteRange + self.bags[bagIdx].GetValue()
            self.roulette.append(self.rouletteRange)

    def DrawBags(self):
        idxOfBagsForReproduction = []
        while(len(idxOfBagsForReproduction) < (len(self.bags)/2) ):
            print "inside DrawBags"
            idxOfBagForReproduction = self.FindBagFromRange()
            if not(idxOfBagForReproduction in idxOfBagsForReproduction):
                idxOfBagsForReproduction.append(idxOfBagForReproduction)
        return idxOfBagsForReproduction
            
    def FindBagFromRange(self):
            randRange = random.randint(0, self.rouletteRange - 1)
            for bagIdx in range(0, len(self.bags)):
                if(self.roulette[bagIdx] > randRange):
                    return bagIdx