from Bag import Bag
import random
import copy

class BagsController():
    def __init__(self, bagParams):
        self.bagParams = bagParams
        self.bags = []
        self.FillBags()
        self.OrderBags()
        
    def PrintValues(self):
        for bagIdx in range(0, len(self.bags)):
            print "bag[" + str(bagIdx) + "] = " + str(self.bags[bagIdx].GetValueSum()) 
            
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
            print "bag.GetValueSum" + str(bag.GetValueSum())
            self.bags.append(bag)
            
    def OrderBags(self):
        isShiftedBag = True;
        while(isShiftedBag):
            isShiftedBag = False
            for bagIdx in range(1, len(self.bags)):
                if(self.bags[bagIdx - 1].GetValueSum() > self.bags[bagIdx].GetValueSum()):
                    tempBag = self.bags[bagIdx];
                    self.bags[bagIdx] = self.bags[bagIdx - 1];
                    self.bags[bagIdx - 1] = tempBag;
                    isShiftedBag = True 
                    
    def FindMostValuable(self):
        bigestValue = 0;
        mostValuableIdx = 0;
        for bagIdx in range(0, len(self.bags)):
            valueOfActualBag = self.bags[bagIdx].GetValueSum()
            if( valueOfActualBag > bigestValue):
                mostValuableIdx = bagIdx
                bigestValue = valueOfActualBag
        return bigestValue
    
    def RemoveLeastValuable(self):
        numOfBags = len(self.bags)
        for bagIdx in range(20,numOfBags):
            self.bags.pop(0)

    def RemoveBags(self):
        for i in range(0, len(self.bags)):
            self.bags.pop()
            
    def AppendBag(self,
                  copyOfBag):
        self.bags.append(copyOfBag)

    def GetCopyOfBags(self):
        return copy.deepcopy(self.bags)
    
    def CreateNewBag(self):
        return Bag(self.bagParams.maxWeightOfBag)






                    
        