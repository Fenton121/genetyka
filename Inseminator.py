import random
import copy
class Inseminator():
    def __init__(self,
                 bags, 
                 idxOfBagsForRepro):
        self.bags              = bags;
        self.idxOfBagsForRepro = idxOfBagsForRepro;
        self.crossProbability  = 60;
        self.bagsAfterReproduction = []
             
    def IsReadyForCross(self):
        randomInt = random.randint(1, 100)
        if(randomInt < self.crossProbability):
            return True
        else:
            return False
        
            
    def IsNotTheSameElements(self,
                             elemIdxs,
                             elemIdxsSecondBag):
        if not( elemIdxsSecondBag in elemIdxs):
            return True
        else:
            return False
        
    def JoinElementInOneBag(self,
                            firstBag,
                            secondBag):
        numOfElemFirstBag = firstBag.GetNumOfElements()
        valueSecondBag, weightSecondBag, elemIdxsSecondBag, numOfElemSecondBag = secondBag.GetParameters()
        
        
        idxForExtraction = random.randint(0, numOfElemFirstBag - 1)
        firstBag.ExtractElements(idxForExtraction)
        isNotOverloaded = True;
        while(isNotOverloaded and (numOfElemSecondBag > 0)):

            randElemIdx = random.randint(0, secondBag.GetNumOfElements() - 1)
            if not (elemIdxsSecondBag[randElemIdx] in firstBag.GetElementIdxs()):
                isNotOverloaded = firstBag.AddElement(weightSecondBag[randElemIdx],
                                                      valueSecondBag[randElemIdx],
                                                      elemIdxsSecondBag[randElemIdx])
            valueSecondBag.pop(randElemIdx)
            weightSecondBag.pop(randElemIdx)
            elemIdxsSecondBag.pop(randElemIdx)
            numOfElemSecondBag = numOfElemSecondBag - 1;
        self.bagsAfterReproduction.append(firstBag)
        
    def MixBags(self,
                idxsOfTwoBag):
        firstBag  = self.bags[idxsOfTwoBag[0]]
        secondBag = self.bags[idxsOfTwoBag[1]]
    
        
        self.JoinElementInOneBag(firstBag, secondBag)
        self.JoinElementInOneBag(secondBag, firstBag)
  
    def CrossBags(self):
        for bagIdx in range(0, len(self.idxOfBagsForRepro)):
            isCross = self.IsReadyForCross()
            idxsOfTwoBag = self.idxOfBagsForRepro[bagIdx]
            if(isCross):
                self.MixBags(idxsOfTwoBag)
            else:
                self.bagsAfterReproduction.append(self.bags[idxsOfTwoBag[0]])
                self.bagsAfterReproduction.append(self.bags[idxsOfTwoBag[1]])
        return copy(self.bagsAfterReproduction)