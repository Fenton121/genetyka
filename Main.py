from GeneticBags import GeneticBags
from DataExtractor import *

if __name__ == "__main__":
    
    bagParameters = GetElementsFromFile()
    geneticBags = GeneticBags(bagParameters)
    geneticBags.StartProcessing()
    




