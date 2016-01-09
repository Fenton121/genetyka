import random
import copy

class BagMixer():
    def __init__(self,
                 bagsController):
        self.bagsController = bagsController
        self.crossProbability = 60
        
    def IsReadyForCross(self):
        randomInt = random.randint(1, 100)
        if(randomInt <= self.crossProbability):
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
         
    def AddElementsFromOneBagToAnother(self,
                                       bagWhichContainElementToMove,
                                       idxOfElementToMove,
                                       numOfElem,
                                       mixedBag):
        
        
        isNotOverloaded = True;
        while( isNotOverloaded and (idxOfElementToMove < numOfElem)):
            weight, value, elementIdxs = bagWhichContainElementToMove.GetElement(idxOfElementToMove)
            isNotOverloaded = mixedBag.AddElement(weight,
                                                  value,
                                                  elementIdxs)
            idxOfElementToMove = idxOfElementToMove + 1
            
    def MixTwoBag(self,
                 firstBag,
                 secondBag):
        numOfElemFirstBag   = firstBag.GetNumOfElements()
        numOfElemeSecondBag = secondBag.GetNumOfElements()
        
        idxForExtractionFirstBag  = random.randint(0, numOfElemFirstBag - 1)
        idxForExtractionSecondBag = random.randint(0, numOfElemeSecondBag - 1)
        
        mixedFirstBag  = firstBag.ExtractElements(idxForExtractionFirstBag)
        mixedSecondBag = secondBag.ExtractElements(idxForExtractionSecondBag)
        
        print 'mixedFirstBag' + str(mixedFirstBag)
        print 'mixedSecondBag' + str(mixedSecondBag)
        self.AddElementsFromOneBagToAnother(secondBag,
                                            idxForExtractionSecondBag,
                                            numOfElemeSecondBag,
                                            mixedFirstBag)

        self.AddElementsFromOneBagToAnother(firstBag,
                                            idxForExtractionSecondBag,
                                            numOfElemFirstBag,
                                            mixedSecondBag)
        
        self.bagsController.AppendBag(mixedFirstBag)
        self.bagsController.AppendBag(mixedSecondBag)
         

        
    def MixBags(self,
                idxOfBagsForRepro):
        copyOfBags = self.bagsController.GetCopyOfBags()
        self.bagsController.RemoveBags()
    
        
        for bagIdx in range(0, len(copyOfBags)):
            isCross = self.IsReadyForCross()
            drawIdx = idxOfBagsForRepro[bagIdx]
            if(isCross):
                self.MixTwoBag(copyOfBags[bagIdx],
                               copyOfBags[drawIdx])
            else:
                self.bagsController.AppendBag(copyOfBags[bagIdx])
                 
         

  
