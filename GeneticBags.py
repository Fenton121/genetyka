from Bag import Bag

from copy import copy
from BagMixer import BagMixer
from BagsController import BagsController
from CrossController import CrossController

class GeneticBags():
    def __init__(self,
                 bagParameters):
        self.bagsController = BagsController(bagParameters)
        self.crossController = CrossController(self.bagsController)
        self.idxOfBagsForReproduction = []
        
        
    def StartProcessing(self):
        bigestValue = self.bagsController.FindMostValuable()
        self.bagsController.PrintValues()
        for crossIdx in range(0, 1):
            self.crossController.CrossBags()
            self.bagsController.OrderBags()
            self.bagsController.RemoveLeastValuable()
            self.bagsController.FindMostValuable()
            self.bagsController.PrintValues()
        
            