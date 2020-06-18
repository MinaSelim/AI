import csv
import Utility

def getModel(filename):
    fileData = open(filename,"rt", encoding="utf-8")
    wordsInModel = dict()
    for row in fileData:
        rowList = row.split()
        wordsInModel[rowList[1]] = rowList
    
    return wordsInModel



def getTestData(filename, year): 
    csvData = open(filename, "rt", encoding="utf-8")
    reader = csv.reader(csvData)

    testData = []

    first = True
    for row in reader:
        if first:
            first = False
            continue
        if int(row[9]) == year:
            testData.append([row[2],row[3]])
    return testData


def getData(filename, types, year):
  #  csvData = open(filename, "rt", encoding="utf-8")
  #  reader = csv.reader(csvData)
    vocabularyDict = dict()
    categDict = dict()

    csvData = open(filename, "rt", encoding="utf-8")
    reader = csv.reader(csvData)

    for wordType in types:
        categDict[wordType] = dict()

    first = True
    for row in reader:
        if first:
            first = False
            continue
        if int(row[9]) == year:
            words = row[2].split()
            for word in words :
                addToWordDict(vocabularyDict, word)
                addToWordDict(categDict[row[3]],word)
#        else:
#            words = row[2].split()
 #           for word in words :
 #               if vocabularyDict.get(word.lower()) is None:
 #                   vocabularyDict[word.lower()] = 0
 
    #print(vocabularyDict)
    #print(wordDict)

    csvData.close()

    return (vocabularyDict,categDict)

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