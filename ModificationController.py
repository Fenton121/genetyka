from Bag import Bag
from Roulette import Roulette
from BagMixer import BagMixer
import random

class ModificationController():
    def __init__(self, bagsController):
        self.bagsController = bagsController
        self.modificationProbability = 40
        
    def IsReadyForModification(self):
        randomInt = random.randint(1, 100)
        if(randomInt <= self.modificationProbability):
            return True
        else:
            return False
        
    def ModificateBags(self):
        numOfBags = self.bagsController.GetNumOfBag()
        for bagIdx in range(0, numOfBags):
            isModificate = self.IsReadyForModification()
            if(isModificate):
                self.bagsController.ModBag(bagIdx)
        
        


         
        
        