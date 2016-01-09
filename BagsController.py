from Bag import Bag
import random

class BagsController():
    def __init__(self, bagParams):
        self.bagParams = bagParams
        self.bags = []
        self.FillBags()
        self.OrderBags()
        
    def PrintValues(self):
        for bagIdx in range(0, len(self.bags)):
            print "bag[" + str(bagIdx) + "] = " + str(self.bags[bagIdx].GetValue()) 
            
    def FillBags(self):
        for bagIdx in range(0, self.bagParams.numOfBags):
            bag = Bag(self.bagParams.maxWeightOfBag)
            isNotOverloaded = True
            while(isNotOverloaded):
                elementIdxRandom =  random.randint(0, self.bagParams.numOfElements - 1)
                weightOfElement, valueOfElement = self.bagParams.elements[elementIdxRandom].GetWeightAndValue()
                isNotOverloaded = bag.AddElement(weightOfElement,
                                                 valueOfElement,
                                                 elementIdxRandom)
            self.bags.append(bag)
            
    def OrderBags(self):
        isShiftedBag = True;
        while(isShiftedBag):
            isShiftedBag = False
            for bagIdx in range(1, len(self.bags)):
                if(self.bags[bagIdx - 1].GetValue() > self.bags[bagIdx].GetValue()):
                    tempBag = self.bags[bagIdx];
                    self.bags[bagIdx] = self.bags[bagIdx - 1];
                    self.bags[bagIdx - 1] = tempBag;
                    isShiftedBag = True 
                    
    def FindMostValuable(self):
        bigestValue = 0;
        mostValuableIdx = 0;
        for bagIdx in range(0, len(self.bags)):
            valueOfActualBag = self.bags[bagIdx].GetValue()
            if( valueOfActualBag > bigestValue):
                mostValuableIdx = bagIdx
                bigestValue = valueOfActualBag
        return bigestValue
    
    def RemoveLeastValuable(self):
        for bagIdx in range(0,10):
            self.bags.pop(0)
        
        