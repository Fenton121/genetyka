from GeneticBags import GeneticBags
from DataExtractor import *

if __name__ == "__main__":
    elements, numOfBags, maxWeightOfBag, numOfElements = GetElementsFromFile()
    
    geneticBags = GeneticBags(elements,
                              numOfBags,
                              maxWeightOfBag,
                              numOfElements)
    geneticBags.StartProcessing()
    




