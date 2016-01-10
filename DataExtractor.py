from Element import Element
from BagParams import BagParams


class DataExtractor():
    def __init__(self):
        self.output = open('output', 'w')
        
    def GetElementsFromFile(self):
    
        bagParams = BagParams()
     
        data = open('data').readlines()
        bagParams.maxWeightOfBag = int(data[0].rstrip())
        bagParams.numOfBags      = int(data[1].rstrip())
        
        numOfElements = len(data)
        bagParams.numOfElements  = numOfElements - 3
        
    
        for elementIdx in range(3, numOfElements):
            valueWeight = data[elementIdx].rstrip()
            valueWeight = valueWeight.split()
            value  = int(valueWeight[0])
            weight = int(valueWeight[1])
            newElement = Element(weight, value)
            bagParams.elements.append(newElement);
            
        
        return bagParams
    
    def WriteActualTheBestBag(self,
                              bag,
                              iteration,
                              actualValue):
        numOfElements = bag.GetNumOfElements()
        values = bag.GetValues()
        weights = bag.GetWeight()
        
        self.output.write("ITEERATION = " + str(iteration) + ", NumOfElements =" + str(numOfElements) + " All Elements Value =" + str(actualValue) +  "\n")
        
        for elemIdx in range(0, numOfElements):
            self.output.write("    Element Indeks = " + str(elemIdx) + " Value = " + str(values[elemIdx]) + " Weight = " + str(weights[elemIdx]) + "\n")
        
    def CloseOutputFile(self):
        self.output.close()