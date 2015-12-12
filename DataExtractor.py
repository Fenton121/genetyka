from Element import Element

def GetElementsFromFile():
    elements = []
    data = open('data').readlines()
    numOfElements = len(data)
    maxWeightOfBag = int(data[0].rstrip())
    numOfBags   = int(data[1].rstrip())
    for elementIdx in range(3, numOfElements):
        valueWeight = data[elementIdx].rstrip()
        valueWeight = valueWeight.split()
        value  = int(valueWeight[0])
        weight = int(valueWeight[1])
        newElement = Element(weight, value)
        elements.append(newElement);
    return elements, numOfBags, maxWeightOfBag