from GeneticBags import GeneticBags
from DataExtractor import *
from DataExtractor import DataExtractor

if __name__ == "__main__":
    dataExtractor = DataExtractor()
    bagParameters = dataExtractor.GetElementsFromFile()
    geneticBags = GeneticBags(bagParameters,
                              dataExtractor)
    geneticBags.StartProcessing()
    




