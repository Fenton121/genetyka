from Bag import Bag
import random
from copy import copy
from Roulette import Roulette
from Inseminator import Inseminator

class GeneticBags():
    def __init__(self,
                 elements,
                 numOfBags,
                 maxWeightOfBag,
                 numOfElements):
        self.elements       = elements;
        self.numOfBags      = numOfBags;
        self.maxWeightOfBag = maxWeightOfBag
        self.numOfElements  = numOfElements;
        self.bags = []
        self.crossProbability = 60;
        self.idxOfBagsForReproduction = []
        
    def PrintValueBags(self):
        for bagIdx in range(0, self.numOfBags):
            print "self.bags["+str(bagIdx)+"] = " + str(self.bags[bagIdx].GetValue())
            
    def FillBags(self):
        for bagIdx in range(0, self.numOfBags):
            bag = Bag(self.maxWeightOfBag)
            isNotOverloaded = True
            while(isNotOverloaded):
                elementIdxRandom =  random.randint(0, self.numOfElements - 1)
                weightOfElement, valueOfElement = self.elements[elementIdxRandom].GetWeightAndValue()
                isNotOverloaded = bag.AddElement(weightOfElement,
                                                 valueOfElement,
                                                 elementIdxRandom)
            self.bags.append(bag)
            
    def OrderBags(self):
        isShiftedBag = True;
        while(isShiftedBag):
            isShiftedBag = False
            for bagIdx in range(1, self.numOfBags):
                if(self.bags[bagIdx - 1].GetValue() > self.bags[bagIdx].GetValue()):
                    tempBag = self.bags[bagIdx];
                    self.bags[bagIdx] = self.bags[bagIdx - 1];
                    self.bags[bagIdx - 1] = tempBag;
                    isShiftedBag = True 
                
    def FindMostValuable(self):
        bigestValue = 0;
        mostValuableIdx = 0;
        for bagIdx in range(0, self.numOfBags):
            valueOfActualBag = self.bags[bagIdx].GetValue()
            if( valueOfActualBag > bigestValue):
                mostValuableIdx = bagIdx
                bigestValue = valueOfActualBag
        return bigestValue
    
    
#         
# 
#             
#     def IsReadyForCross(self):
#         randomInt = random.randint(1, 100)
#         if(randomInt < self.crossProbability):
#             return True
#         else:
#             return False
#         
#     def MixTwoBag(self,
#                   bag,
#                   bagForReproduction):
#         numOfElements = bag.GetNumOfElements();
#         randNumOfElementToMix = random.randint(0, numOfElements-1)
#         
#         bag.ExtractElements(randNumOfElementToMix)
#         bag.AddElementsFromOtherBag(bagForReproduction)
#         
#         return bag
#         
#     def MixBags(self,
#                 bagIdx,
#                 bagsForReproduction):
#         bag = copy(self.bags[bagIdx])
#         bagForReproduction = copy(bagsForReproduction[bagIdx])
#         
#         
#         newBag = self.MixTwoBag(bag,
#                                 bagForReproduction)
#         self.bags[bagIdx] = newBag
#         
#     def CrossBags(self,
#                   bagsForReproduction):
# 
#         for bagIdx in range(0, self.numOfBags):
#             isCross = self.IsReadyForCross()
#             if(isCross):
#                 self.MixBags(bagIdx,
#                              bagsForReproduction)
            
            
    def DrawIdxOfBagsForReproduction(self):
        roulette = Roulette(self.bags)
        self.idxOfBagsForReproduction = roulette.DrawBags()
        
    def StartCrossBags(self):
        self.DrawIdxOfBagsForReproduction()
        
        
    def ResetVariable(self):
        self.idxOfBagsForReproduction = []
        inseminator = Inseminator(self.bags,
                                  self.idxOfBagsForReproduction)
        
    def StartProcessing(self):
        self.FillBags()
        self.OrderBags()
        bigestValue = self.FindMostValuable()
        self.PrintValueBags()
        print "bigestValue = " + str(bigestValue)
        self.ResetVariable()
        self.StartCrossBags()
#         for crossIdx in range(0, 1):
#             self.StartCrossBags()
#             bigestValue = self.FindMostValuable()
#             print "crossIdx " + str(crossIdx) + " bigestValue = " + str(bigestValue)
            