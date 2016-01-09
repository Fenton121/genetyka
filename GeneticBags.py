# from Bag import Bag

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
#         print 'POCZATEK PROGRAMU'
#         self.bagsController.PrintNumOfElements()
#         self.bagsController.PrintWeights()
        for crossIdx in range(0, 100):
            self.crossController.CrossBags()
            self.bagsController.OrderBags()
            
            self.bagsController.RemoveLeastValuable()
            bigestValue = self.bagsController.FindMostValuable()
            print "bigestValue = " + str(bigestValue)
        
#         print 'KONIEC PROGRAMU'
#         self.bagsController.PrintNumOfElements()