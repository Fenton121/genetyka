import random

class Bag():
    def __init__(self,
                 maxWeightOfBag):
        self.weight = []
        self.value = []
        self.elementIdxs = []
        self.maxWeightOfBag = maxWeightOfBag
        
    def AddElement(self,
                   weight,
                   value,
                   elementIdx):
        if( (sum(self.weight) + weight) < self.maxWeightOfBag):
            self.weight.append(weight)
            self.value.append(value)
            self.elementIdxs.append(elementIdx)
            return True
        else:
            return False
        
    def ExtractElements(self,
                        elementIdx):
        self.weight = self.weight[0:elementIdx]
        self.value = self.value[0:elementIdx]
        self.elementIdxs = self.elementIdxs[0:elementIdx]
        
    def IsNotTheSameElements(self,
                             elemIdxBagForRepr):
        print "elemIdxBagForRepr" + str(elemIdxBagForRepr)
        print "self.elementIdxs" + str(self.elementIdxs)
        if( elemIdxBagForRepr in self.elementIdxs):
            print "return False"
            return False
        else:
            return True
        
    def AddElementsFromOtherBag(self,
                                bagForReproduction):
        
        numOfElemInNewBag = bagForReproduction.GetNumOfElements()
        valueBagForRepr, weightBagForRepr, elemIdxBagForRepr = bagForReproduction.GetValueWeightElementIdxs()
        isNotOverloaded = True;
        
        while(isNotOverloaded):
            print "isNotOverloaded" + str(isNotOverloaded)
            randElemIdx = random.randint(0, numOfElemInNewBag - 1)
            isNotTheSameElements = self.IsNotTheSameElements(elemIdxBagForRepr[randElemIdx])
            print "isNotTheSameElements" + str(isNotTheSameElements)
            if(isNotTheSameElements):
                isNotOverloaded = self.AddElement(weightBagForRepr[randElemIdx],
                                                  valueBagForRepr[randElemIdx],
                                                  elemIdxBagForRepr[randElemIdx])

                
        
    def GetValueWeightElementIdxs(self):
        return self.value, self.weight, self.elementIdxs
    
    def GetValue(self):
        return sum(self.value)
    
    def GetWeight(self):
        return sum(self.weight)
    
    def GetNumOfElements(self):
        return len(self.elementIdxs);