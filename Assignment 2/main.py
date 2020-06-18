import FileReader
import Processing
import Utility
import ModelGenerator
from collections import OrderedDict 

fileToRead = "hns_2018_2019.csv"
vocabFile = "vocabulary.txt"

types = ["story","ask_hn","show_hn","poll"]
smoothingValue = 0.5

def runExperiment(filter,removedWordFile,modelfile,resultFile,vocabFile):
    data = FileReader.getData(fileToRead,types,2018)

    vocabDict = data[0]
    catDict = data[1]

    sortedVocabDict = OrderedDict(sorted(vocabDict.items()))

    removedWords = Processing.filterAndRemove(sortedVocabDict,catDict, filter)

    Utility.outputListToFile(sortedVocabDict.keys(), vocabFile)
    Utility.outputListToFile(removedWords, removedWordFile)

    Processing.smoothAllCategories(vocabDict, catDict, smoothingValue)

    ModelGenerator.outputModelToFile(modelfile,sortedVocabDict,catDict,smoothingValue)

    model = FileReader.getModel(modelfile)

    testData = FileReader.getTestData(fileToRead,2019)

    return ModelGenerator.outputBaysianClassification(resultFile,testData,model,types,sortedVocabDict,catDict)

print(str(runExperiment(Processing.baselineFilter, "text/remove_word.txt", "text/model-2018.txt", "text/baseline-result.txt" , "vocabulary.txt")))
print("\n")
print(str(runExperiment(Processing.stopFilter, "text/stopword-remove_word.txt", "text/stopword-model-2018.txt", "text/stopword-result.txt", "stopword-vocabulary.txt")))
print("\n")
print(str(runExperiment(Processing.wordLengthFilter, "text/wordlength-remove_word.txt", "text/wordlength-model-2018.txt", "text/wordlength-result.txt", "wordlength-vocabulary.txt")))
print("\n")

f1 = runExperiment(Processing.removeSmallerOrEqualThanFilter1, "text/f1-remove_word.txt", "text/f1-model-2018.txt", "text/f1-baseline-result.txt", "text/f1-vocabulary.txt" )
print(str(f1) + "\n")

f5 = runExperiment(Processing.removeSmallerOrEqualThanFilter5, "text/f5-remove_word.txt", "text/f5-model-2018.txt", "text/f5-baseline-result.txt" , "text/f10-vocabulary.txt")
print(str(f5) + "\n")

f10 = runExperiment(Processing.removeSmallerOrEqualThanFilter10, "text/f10-remove_word.txt", "text/f10-model-2018.txt", "text/f10-baseline-result.txt", "text/f15-vocabulary.txt" )
print(str(f10) + "\n")

f15 = runExperiment(Processing.removeSmallerOrEqualThanFilter15, "text/f15-remove_word.txt", "text/f15-model-2018.txt", "text/f15-baseline-result.txt", "text/f20-vocabulary.txt" )
print(str(f15) + "\n")

f20 = runExperiment(Processing.removeSmallerOrEqualThanFilter20, "text/f20-remove_word.txt", "text/f20-model-2018.txt", "text/f20-baseline-result.txt" , "text/f25-vocabulary.txt")
print(str(f20) + "\n")