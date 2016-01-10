# from Bag import Bag

from copy import copy
from BagMixer import BagMixer
from BagsController import BagsController
from CrossController import CrossController
from ModificationController import ModificationController
import matplotlib.pyplot as plt

class GeneticBags():
    def __init__(self,
                 bagParameters,
                 dataExtractor):
        self.bagsController = BagsController(bagParameters)
        self.crossController = CrossController(self.bagsController)
        self.modificationController = ModificationController(self.bagsController)
        self.idxOfBagsForReproduction = []
        self.dataExtractor = dataExtractor
        
        
    def StartProcessing(self):
        maxValue = 0
        actualValue = self.bagsController.GetMostValuable()
        valuesAllIteration = []
        for crossIdx in range(0, 1000):
            self.modificationController.ModificateBags()
            self.bagsController.OrderBags()
            self.crossController.CrossBags()
            self.bagsController.OrderBags()
            self.bagsController.RemoveLeastValuable()
             
             
            actualValue = self.bagsController.GetMostValuable()
            
            valuesAllIteration.append(actualValue)
            if(actualValue > maxValue):
                maxValue = actualValue
                
            print 'crossIdx = ' + str(crossIdx) + 'actualValue = ' + str(actualValue) + ' maxValue = ' + str(maxValue)
            self.dataExtractor.WriteActualTheBestBag(self.bagsController.GetFirstBag(),
                                                     crossIdx,
                                                     actualValue)
        plt.figure(figsize=(20,10))
        plt.plot(valuesAllIteration)
        plt.xlabel('Iterations')
        plt.ylabel('Values, Max Value = ' + str(maxValue))
        plt.title("Population = 200, CrossProbability = 0.6, MutationProbability = 0.4, Roulette - 2 Most Valuable")
        plt.savefig("dupa.png", format='png')
        plt.show()
        plt.close()
        
        self.dataExtractor.CloseOutputFile()