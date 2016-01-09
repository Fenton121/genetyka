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
                                       mixedBag):
        
        isNotOverloaded = True;
        isElements = True
        while(isElements): 
            weight, value, elementIdxs = bagWhichContainElementToMove.GetRandElement()
            isNotOverloaded = mixedBag.AddElement(weight,
                                                  value,
                                                  elementIdxs)
            isElements = bagWhichContainElementToMove.ContainElements()
            
            
    def MixTwoBag(self,
                  firstBag,
                  secondBag):
        
        numOfElemFirstBag   = firstBag.GetNumOfElements()
        numOfElemeSecondBag = secondBag.GetNumOfElements()
    
        numOfExtrElemFirstBag  = random.randint(1, numOfElemFirstBag - 1)
        numOfExtrElemSecondBag = random.randint(1, numOfElemeSecondBag - 1)
        
        mixedFirstBag  = copy.deepcopy(firstBag)
        mixedSecondBag = copy.deepcopy(secondBag)
        
        mixedFirstBag.ExtractElements(numOfExtrElemFirstBag)
        mixedSecondBag.ExtractElements(numOfExtrElemSecondBag)
        
        
        self.AddElementsFromOneBagToAnother(copy.deepcopy(secondBag),
                                            mixedFirstBag)

        self.AddElementsFromOneBagToAnother(copy.deepcopy(firstBag),
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
#         self.bagsController.PrintNumOfElements()
                 
         

  
