import random

class Bag():
    def __init__(self,
                 maxWeightOfBag):
        self.weight = []
        self.value = []
        self.elementIdxs = []
        self.maxWeightOfBag = maxWeightOfBag
        
        
    def ExtractElements(self,
                        idxForExtraction):
        
        numOfElemForExtraction = self.GetNumOfElements() - idxForExtraction - 1
        
        for elemIdx in range(0, numOfElemForExtraction):
            self.weight.pop()
            self.value.pop()
            self.elementIdxs.pop()
        
    def IsNotTheSameElem(self,
                         elemIdx):
        if not (elemIdx in self.elementIdxs):
            return True
        else:
            return False
    
    def AddElement(self,
                   weight,
                   value,
                   elementIdx):
        if( ((sum(self.weight) + weight) < self.maxWeightOfBag) & self.IsNotTheSameElem(elementIdx)):
            self.weight.append(weight)
            self.value.append(value)
            self.elementIdxs.append(elementIdx)
            return True
        else:
            return False
        
    def GetElement(self,
                   elementIdx):
        
        return self.weight[elementIdx], self.value[elementIdx], self.elementIdxs[elementIdx]
        
    
    def GetValueSum(self):
        return sum(self.value)
    
    def GetWeightSum(self):
        return sum(self.weight)
    
    def GetNumOfElements(self):
        return len(self.elementIdxs)
    
    def GetElementIdxs(self):
        return self.elementIdxs