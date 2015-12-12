class Inseminator():
    def __init__(self,
                 bags, 
                 idxOfBagsForRepro):
        self.bags              = bags;
        self.idxOfBagsForRepro = idxOfBagsForRepro;

#         
# 
#             
#     def IsReadyForCross(self):
#         randomInt = random.randint(1, 100)
#         if(randomInt < self.crossProbability):
#             return True
#         else:
#             return False
#         
#     def MixTwoBag(self,
#                   bag,
#                   bagForReproduction):
#         numOfElements = bag.GetNumOfElements();
#         randNumOfElementToMix = random.randint(0, numOfElements-1)
#         
#         bag.ExtractElements(randNumOfElementToMix)
#         bag.AddElementsFromOtherBag(bagForReproduction)
#         
#         return bag
#         
#     def MixBags(self,
#                 bagIdx,
#                 bagsForReproduction):
#         bag = copy(self.bags[bagIdx])
#         bagForReproduction = copy(bagsForReproduction[bagIdx])
#         
#         
#         newBag = self.MixTwoBag(bag,
#                                 bagForReproduction)
#         self.bags[bagIdx] = newBag
#         
    def CrossBags(self):
        for bagIdx in range(0, len(self.idxOfBagsForRepro)):
            print "bagIdx =" + str(bagIdx)
#             isCross = self.IsReadyForCross()
#             if(isCross):
#                 self.MixBags(bagIdx,
#                              bagsForReproduction)