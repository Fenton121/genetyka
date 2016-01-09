import random
import copy

class BagMixer():
    def __init__(self,
                 bags):
        self.bags = bags;
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
         
    def MixTwoBag(self,
                 firstBag,
                 secondBag):
        
#         numOfElemFirstBag = firstBag.GetNumOfElements()
#         valueSecondBag, weightSecondBag, elemIdxsSecondBag, numOfElemSecondBag = secondBag.GetParameters()
#         idxForExtraction = random.randint(0, numOfElemFirstBag - 1)
#         firstBag.ExtractElements(idxForExtraction)
#         isNotOverloaded = True;
#         while(isNotOverloaded and (numOfElemSecondBag > 0)):
#  
#             randElemIdx = random.randint(0, secondBag.GetNumOfElements() - 1)
#             if not (elemIdxsSecondBag[randElemIdx] in firstBag.GetElementIdxs()):
#                 isNotOverloaded = firstBag.AddElement(weightSecondBag[randElemIdx],
#                                                       valueSecondBag[randElemIdx],
#                                                       elemIdxsSecondBag[randElemIdx])
#             valueSecondBag.pop(randElemIdx)
#             weightSecondBag.pop(randElemIdx)
#             elemIdxsSecondBag.pop(randElemIdx)
#             numOfElemSecondBag = numOfElemSecondBag - 1;
#         self.bagsAfterReproduction.append(firstBag)
         
    def RemoveBags(self):
        for i in range(0, len(self.bags)):
            self.bags.pop()
        
    def MixBags(self,
                idxOfBagsForRepro):
        copyOfBags = copy.deepcopy(self.bags)
        self.RemoveBags()
        
        
        print 'idxOfBagsForRepro' + str(idxOfBagsForRepro);
        
        for bagIdx in range(0, len(copyOfBags)):
            isCross = self.IsReadyForCross()
            drawIdx = idxOfBagsForRepro[bagIdx]
            if(isCross):
                self.MixTwoBag(copyOfBags[bagIdx],
                               copyOfBags[drawIdx])
            else:
                self.bags.append(copyOfBags[bagIdx])
                 
         

  
