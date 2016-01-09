from Element import Element
from BagParams import BagParams

def GetElementsFromFile():
    
    bagParams = BagParams()
 
    data = open('data4').readlines()
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