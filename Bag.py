import random

class Bag():
    def __init__(self,
                 maxWeightOfBag):
        self.weight = []
        self.value = []
        self.elementIdxs = []
        self.maxWeightOfBag = maxWeightOfBag
        
        
    def ExtractElements(self,
                        numOfElemToExtr):
        for elemIdx in range(0, numOfElemToExtr):
            numOfElement = len(self.elementIdxs)
            randomIdx = random.randint(0, numOfElement - 1)
            self.weight.pop(randomIdx)
            self.value.pop(randomIdx)
            self.elementIdxs.pop(randomIdx)
        
    def IsTheSameElem(self,
                         elemIdx):
        return elemIdx in self.elementIdxs
    
    
    def AddElement(self,
                   weight,
                   value,
                   elementIdx):
        if( (sum(self.weight) + weight) <= self.maxWeightOfBag) :
            if not (self.IsTheSameElem(elementIdx)):
                self.weight.append(weight)
                self.value.append(value)
                self.elementIdxs.append(elementIdx)
            return True
        else:
            return False
        
    def ContainElements(self):
        numOfElement = len(self.elementIdxs)
        if(numOfElement > 0):
            return True
        else:
            return False
        
    def GetRandElement(self):
        numOfElement = len(self.elementIdxs)
        randomIdx = random.randint(0, numOfElement - 1)
        
        weight     = self.weight[randomIdx]
        value      = self.value[randomIdx]
        elementIdx = self.elementIdxs[randomIdx]
        self.weight.pop(randomIdx)
        self.value.pop(randomIdx)
        self.elementIdxs.pop(randomIdx)
        
        return weight, value, elementIdx
        
    def RemoveRandElement(self):
        numOfElement = len(self.elementIdxs)
        randomIdx = random.randint(0, numOfElement - 1)
        
        self.weight.pop(randomIdx)
        self.value.pop(randomIdx)
        self.elementIdxs.pop(randomIdx)
        
    def GetValueSum(self):
        return sum(self.value)
    
    def GetElementIdxs(self):
        return self.elementIdxs
    def GetWeight(self):
        return self.weight
    def GetWeightSum(self):
        return sum(self.weight)
    
    def GetNumOfElements(self):
        return len(self.elementIdxs)
    
    def GetElementIdxs(self):
        return self.elementIdxs