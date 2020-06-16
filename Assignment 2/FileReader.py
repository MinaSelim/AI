import csv
import Utility

def getData(filename, types):
  #  csvData = open(filename, "rt", encoding="utf-8")
  #  reader = csv.reader(csvData)
    vocabularyDict = dict()
    wordDict = dict()

    csvData = open(filename, "rt", encoding="utf-8")
    reader = csv.reader(csvData)

    for wordType in types:
        wordDict[wordType] = dict()

    first = True
    for row in reader:
        if first:
            first = False
            continue
        words = row[2].split()
        for word in words :
            addToWordDict(vocabularyDict, word)
            addToWordDict(wordDict[row[3]],word)
 
    #print(vocabularyDict)
    #print(wordDict)

    csvData.close()

    return (vocabularyDict,wordDict)

def addToWordDict(wordDict, word):
    if wordDict.get(word.lower()) is None:
        wordDict[word.lower()] = 1
    else:
        wordDict[word.lower()] += 1

def getAllTypesFromCsvData(reader):
    types = []
    first = True
    for row in reader:
        if first:
            first = False
            continue
        if not(Utility.listContains(types, row[3])):
            types.append(row[3])
    return types

#print(getData("hns_2018_2019.csv"))