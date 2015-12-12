from GeneticBags import GeneticBags
from DataExtractor import *

if __name__ == "__main__":
    elements, numOfBags, maxWeightOfBag = GetElementsFromFile()
    
    geneticBags = GeneticBags(elements,
                              numOfBags,
                              maxWeightOfBag)
    geneticBags.StartProcessing()
    




