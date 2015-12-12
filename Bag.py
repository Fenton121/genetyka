class Bag():
    def __init__(self,
                 maxWeightOfBag):
        self.weight = 0
        self.value = 0
        self.elementIdx = []
        self.maxWeightOfBag = maxWeightOfBag
        
    def AddElement(self,
                   weight,
                   value,
                   elementIdx):
        if( (self.weight + weight) < self.maxWeightOfBag):
            self.weight = self.weight + weight
            self.value = self.value + value
            self.elementIdx.append(elementIdx)
            return True
        else:
            return False
        