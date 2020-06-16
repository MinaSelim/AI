import FileReader
import Processing
import Utility
import ModelGenerator
from collections import OrderedDict 

fileToRead = "hns_2018_2019.csv"
outputfile = "model-2018.txt"
vocabFile = "vocabulary.txt"
removedWordFile = "remove_word.txt"

types = ["story","ask_hn","show_hn","poll"]
smoothingValue = 0.5
year2018 = 2018

data = FileReader.getData(fileToRead,types)

vocabDict = data[0]
catDict = data[1]

sortedVocabDict = OrderedDict(sorted(vocabDict.items()))

removedWords = Processing.filterAndRemove(sortedVocabDict,catDict)

Utility.outputListToFile(sortedVocabDict.keys(), vocabFile)
Utility.outputListToFile(removedWords, removedWordFile)

Processing.smoothAllCategories(vocabDict, catDict, smoothingValue)

ModelGenerator.outputModelToFile(outputfile,sortedVocabDict,catDict)