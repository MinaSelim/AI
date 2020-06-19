import FileReader
import Processing
import Utility
import ModelGenerator
from collections import OrderedDict 
import Plotter

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

f5 = runExperiment(Processing.removeSmallerOrEqualThanFilter5, "text/f5-remove_word.txt", "text/f5-model-2018.txt", "text/f5-baseline-result.txt" , "text/f5-vocabulary.txt")
print(str(f5) + "\n")

f10 = runExperiment(Processing.removeSmallerOrEqualThanFilter10, "text/f10-remove_word.txt", "text/f10-model-2018.txt", "text/f10-baseline-result.txt", "text/f10-vocabulary.txt" )
print(str(f10) + "\n")

f15 = runExperiment(Processing.removeSmallerOrEqualThanFilter15, "text/f15-remove_word.txt", "text/f15-model-2018.txt", "text/f15-baseline-result.txt", "text/f15-vocabulary.txt" )
print(str(f15) + "\n")

f20 = runExperiment(Processing.removeSmallerOrEqualThanFilter20, "text/f20-remove_word.txt", "text/f20-model-2018.txt", "text/f20-baseline-result.txt" , "text/f20-vocabulary.txt")
print(str(f20) + "\n")

t5 = runExperiment(Processing.removeTopPercentile5, "text/t5-remove_word.txt", "text/t5-model-2018.txt", "text/t5-baseline-result.txt" , "text/t5-vocabulary.txt")
print(str(t5) + "\n")

t10 = runExperiment(Processing.removeTopPercentile10, "text/t10-remove_word.txt", "text/t10-model-2018.txt", "text/t10-baseline-result.txt" , "text/t10-vocabulary.txt")
print(str(t10) + "\n")

t15 = runExperiment(Processing.removeTopPercentile15, "text/t15-remove_word.txt", "text/t15-model-2018.txt", "text/t15-baseline-result.txt" , "text/t15-vocabulary.txt")
print(str(t15) + "\n")

t20 = runExperiment(Processing.removeTopPercentile20, "text/t20-remove_word.txt", "text/t20-model-2018.txt", "text/t20-baseline-result.txt" , "text/t20-vocabulary.txt")
print(str(t20) + "\n")

t25 = runExperiment(Processing.removeTopPercentile25, "text/t25-remove_word.txt", "text/t25-model-2018.txt", "text/t25-baseline-result.txt" , "text/t25-vocabulary.txt")
print(str(t25) + "\n")

f = [f1,f5,f10,f15,f20]
t = [t5,t10,t15,t20,t25]

Plotter.displayStuff(f,t)