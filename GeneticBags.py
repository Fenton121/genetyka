# from Bag import Bag

from copy import copy
from BagMixer import BagMixer
from BagsController import BagsController
from CrossController import CrossController
from ModificationController import ModificationController

class GeneticBags():
    def __init__(self,
                 bagParameters):
        self.bagsController = BagsController(bagParameters)
        self.crossController = CrossController(self.bagsController)
        self.modificationController = ModificationController(self.bagsController)
        self.idxOfBagsForReproduction = []
        
        
    def StartProcessing(self):
        
        maxValue = 0
        bigestValue = self.bagsController.FindMostValuable()
        for crossIdx in range(0, 10000):
            self.modificationController.ModificateBags()
            self.bagsController.OrderBags()
            self.crossController.CrossBags()
            self.bagsController.OrderBags()
            self.bagsController.RemoveLeastValuable()
             
            bigestValue = self.bagsController.FindMostValuable()
            
            if(bigestValue > maxValue):
                maxValue = bigestValue
                
            print 'crossIdx = ' + str(crossIdx) + 'bigestValueActual = ' + str(bigestValue) + ' maxValue = ' + str(maxValue)
                
#                 self.bagsController.PrintElementsIdxs()
#                 self.bagsController.PrintWeights()
#                 self.bagsController.PrintWeightsSum()