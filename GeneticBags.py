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
            
            
    def DrawIdxOfBagsForReproduction(self):
        roulette = Roulette(self.bags)
        self.idxOfBagsForReproduction = roulette.DrawBags()
        
        
    def StartCrossBags(self):
        self.DrawIdxOfBagsForReproduction()
        inseminator = Inseminator(self.bags,
                                  self.idxOfBagsForReproduction)
        self.bags = inseminator.CrossBags()
        print "self.bags = " + str(self.bags)
        
    def ResetVariable(self):
        self.idxOfBagsForReproduction = []

        
    def StartProcessing(self):
        self.FillBags()
        self.OrderBags()
        bigestValue = self.FindMostValuable()
        self.PrintValueBags()
        for crossIdx in range(0, 1):
            self.ResetVariable()
            self.StartCrossBags()
#             bigestValue = self.FindMostValuable()
            print "crossIdx " + str(crossIdx) + " bigestValue = " + str(bigestValue)
            