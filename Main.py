from GeneticBags import GeneticBags
from DataExtractor import *

if __name__ == "__main__":
    weightOfBag, numOfBags, elements = GetElementsFromFile()
    geneticBags = GeneticBags()
    geneticBags.Process()
    




