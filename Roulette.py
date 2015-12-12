class Roulette():
    def __init__(self,
                 bags):
        self.roulette = []
        self.rouletteRange = 0
        
        numOfBags = len(bags)
        for bagIdx in range(0, numOfBags):
            self.rouletteRange = self.rouletteRange + bags[bagIdx].GetValue()
            self.roulette.append(self.rouletteRange)
