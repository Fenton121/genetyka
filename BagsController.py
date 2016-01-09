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
            
    def PrintNumOfElements(self):
        print 'len(self.bags)' + str(len(self.bags))
        for bagIdx in range(0, len(self.bags)):
            print "bag[" + str(bagIdx) + "].NumOfElements = " + str(self.bags[bagIdx].GetNumOfElements()) 
    
    def PrintWeightsSum(self):
        for bagIdx in range(0, len(self.bags)):
            print "bag[" + str(bagIdx) + "].WeightSum = " + str(self.bags[bagIdx].GetWeightSum()) 
    def PrintWeights(self):
        for bagIdx in range(0, len(self.bags)):
            print "bag[" + str(bagIdx) + "].Weight = " + str(self.bags[bagIdx].GetWeight()) 
            
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
                if(self.bags[bagIdx - 1].GetValueSum() < self.bags[bagIdx].GetValueSum()):
                    tempBag = self.bags[bagIdx];
                    self.bags[bagIdx] = self.bags[bagIdx - 1];
                    self.bags[bagIdx - 1] = tempBag;
                    isShiftedBag = True 
                    
    def FindMostValuable(self):
        return self.bags[len(self.bags) - 1].GetValueSum()
    
    def RemoveLeastValuable(self):
        numOfBags = len(self.bags)
        for bagIdx in range(self.bagParams.numOfBags, numOfBags):
            self.bags.pop()

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
    
    def GetNumOfBag(self):
        return len(self.bags)
    
    def ModBag(self,
               bagIdx):
        bagForModification = copy.deepcopy(self.bags[bagIdx])
        bagForModification.RemoveRandElement()
        bagForModification.RemoveRandElement()
        bagForModification.RemoveRandElement()
        
        for idxOfTry in range(0, 100):
            elementIdxRandom =  random.randint(0, self.bagParams.numOfElements - 1)
            weightOfElement, valueOfElement = self.bagParams.elements[elementIdxRandom].GetWeightAndValue()
            bagForModification.AddElement(weightOfElement,
                                          valueOfElement,
                                          elementIdxRandom)
        
        
        self.bags[bagIdx] = bagForModification





                    
        