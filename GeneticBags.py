from Bag import Bag
import random

class GeneticBags():
    def __init__(self,
                 elements,
                 numOfBags,
                 maxWeightOfBag):
        self.elements       = elements;
        self.numOfBags      = numOfBags;
        self.maxWeightOfBag = maxWeightOfBag
        self.bags = []
        
    def FillBags(self):
        for bagIdx in range(0, self.numOfBags):
            bag = Bag(self.maxWeightOfBag)
            isNotOverloaded = True
            while(isNotOverloaded):
                elementIdxRandom =  random.randint(0, self.numOfBags - 1)
                weightOfElement, valueOfElement = self.elements[elementIdxRandom].GetWeightAndValue()
                isNotOverloaded = bag.AddElement(weightOfElement,
                                                 valueOfElement,
                                                 elementIdxRandom)
            self.bags.append(bag)
        
    def StartProcessing(self):
        self.FillBags()