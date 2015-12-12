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
        self.crossProbability = 60;
        
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
            
    def FindMostValuable(self):
        bigestValue = 0;
        mostValuableIdx = 0;
        for bagIdx in range(0, self.numOfBags):
            valueOfActualBag = self.bags[bagIdx].GetValue()
            if( valueOfActualBag > bigestValue):
                mostValuableIdx = bagIdx
                bigestValue = valueOfActualBag
        return bigestValue
    
    def CreateRoulette(self):
        roulette = []
        rouletteRange = 0
        for bagIdx in range(0, self.numOfBags):
            rouletteRange = rouletteRange + self.bags[bagIdx].GetValue()
            roulette.append(rouletteRange)
        return roulette, rouletteRange
    
    
    def FindIdxOfBagsFromRange(self,
                               roulette,
                               rouletteRange,
                               bagIdxForReproduction):

        while(True):
            isFinded = False
            randRange = random.randint(0, rouletteRange - 1)
            print "randRange" + str(randRange)
            print "roulette" + str(roulette)
            
            for bagIdx in range(0, self.numOfBags):
                
                if(roulette[bagIdx] > randRange):
                    if( (bagIdx != bagIdxForReproduction) and (isFinded == False)):
                        print " jest ok !!!" 
                        return self.bags[bagIdx]
                    isFinded = True
                    

    
        
    def DrawBagsForReproduction(self):
        roulette, rouletteRange = self.CreateRoulette()
        bagsForReproduction = []
        for bagIdxForReproduction in range(0, self.numOfBags):
            bagForReproduction = self.FindIdxOfBagsFromRange(roulette,
                                                             rouletteRange,
                                                             bagIdxForReproduction)

            bagsForReproduction.append(bagForReproduction)
        return bagsForReproduction
            
    def IsReadyForCross(self):
        randomInt = random.randint(1, 100)
        if(randomInt < self.crossProbability):
            return True
        else:
            return False
        
    def MixTwoBag(self,
                  bag,
                  bagForReproduction):
        numOfElements = bag.GetNumOfElements();
        randNumOfElementToMix = random.randint(0, numOfElements-1)
        
        bag.ExtractElements(randNumOfElementToMix)
        bag.AddElementsFromOtherBag(bagForReproduction)
        
        return bag
        
    def MixBags(self,
                bagIdx,
                bagsForReproduction):
        bag = self.bags[bagIdx];
        bagForReproduction = bagsForReproduction[bagIdx]
        newBag = self.MixTwoBag(bag,
                                bagForReproduction)
        self.bags[bagIdx] = newBag
        
    def CrossBags(self,
                  bagsForReproduction):

        for bagIdx in range(0, self.numOfBags):
            isCross = self.IsReadyForCross()
            if(isCross):
                self.MixBags(bagIdx,
                             bagsForReproduction)
            
            
            
    def StartCrossBags(self):
        print "StartCrossBags1"
        bagsForReproduction = self.DrawBagsForReproduction()
        print "StartCrossBags2"
        self.CrossBags(bagsForReproduction)
    
    def StartProcessing(self):
        self.FillBags()
        bigestValue = self.FindMostValuable()
        for crossIdx in range(0, 100):
            print "crossIdx1 = " + str(crossIdx)
            self.StartCrossBags()
            print "crossIdx2 = " + str(crossIdx)
            bigestValue = self.FindMostValuable()
            print "crossIdx " + str(crossIdx) + " bigestValue = " + str(bigestValue)
            