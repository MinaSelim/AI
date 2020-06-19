import Utility
import numpy

stopFilterFile = open("stop-words.txt","rt", encoding="utf-8")
stopList = []
for word in stopFilterFile:
    stopList.append(word.rstrip())

def filterAndRemove(vocabDict, categoryDict, filter):
    lstOfRemovedWords = []
    for key in vocabDict.keys():
        if filter(key,vocabDict):
            lstOfRemovedWords.append(key)
    for key in lstOfRemovedWords:
        removeKey(vocabDict,categoryDict,key)
    return lstOfRemovedWords


def smoothAllCategories(vocabDict, categoryDict, smoothingValue):
    for key in categoryDict.keys():
        wordSmoothing(vocabDict, categoryDict[key], smoothingValue)


def wordSmoothing(vocabDict, wordsInCategoryDict, smoothingValue):
    for key in vocabDict.keys():
        vocabDict[key] += smoothingValue
        if wordsInCategoryDict.get(key) is None:
            wordsInCategoryDict[key] = smoothingValue
        else:
            wordsInCategoryDict[key] += smoothingValue

def removeKey(vocabDict,categoryDict,key):
    vocabDict.pop(key,None)
    for categkey in categoryDict.keys():
        categoryDict[categkey].pop(key,None)

def baselineFilter(key,vocabDict):
    return key.find("(") != -1 or key.find(")") != -1 or key.find(".") != -1 or key.find("?") != -1 or key.find("!") != -1 or key.find("“") != -1  or key.find("\"") != -1 \
    or key.find(",") != -1 or key.find("$") != -1 or key.find("‘") != -1 or key.startswith("'")

def stopFilter(key,vocabDict) :
    return Utility.listContains(stopList,key)

def wordLengthFilter(key,vocabDict) :
    return len(key) < 3 or len(key) > 8

def removeSmallerOrEqualThanFilter1(key, vocabDict):
    return removeSmallerOrEqualThanFilter(key, vocabDict, 1)

def removeSmallerOrEqualThanFilter5(key, vocabDict):
    return removeSmallerOrEqualThanFilter(key, vocabDict, 5)

def removeSmallerOrEqualThanFilter10(key, vocabDict):
    return removeSmallerOrEqualThanFilter(key, vocabDict, 10)

def removeSmallerOrEqualThanFilter15(key, vocabDict):
    return removeSmallerOrEqualThanFilter(key, vocabDict, 15)

def removeSmallerOrEqualThanFilter20(key, vocabDict):
    return removeSmallerOrEqualThanFilter(key, vocabDict, 20)

def removeSmallerOrEqualThanFilter(key, vocabDict, value):
    return vocabDict[key] <= value


currentPercentile = 0
currentCutoff = 0

def removeTopPercentile5(key,vocabDict):
    global currentPercentile
    global currentCutoff
    if currentPercentile != 5:
        currentPercentile = 5
        values = vocabDict.values()
        currentCutoff = numpy.percentile(list(values),95)
    return removeTopPercentile(key, vocabDict, currentCutoff)

def removeTopPercentile10(key,vocabDict):
    global currentPercentile
    global currentCutoff
    if currentPercentile != 10:
        currentPercentile = 10
        values = vocabDict.values()
        currentCutoff = numpy.percentile(list(values),90)
    return removeTopPercentile(key, vocabDict, currentCutoff)

def removeTopPercentile15(key,vocabDict):
    global currentPercentile
    global currentCutoff
    if currentPercentile != 15:
        currentPercentile = 15
        values = vocabDict.values()
        currentCutoff = numpy.percentile(list(values),85)
    return removeTopPercentile(key, vocabDict, currentCutoff)

def removeTopPercentile20(key,vocabDict):
    global currentPercentile
    global currentCutoff
    if currentPercentile != 20:
        currentPercentile = 20
        values = vocabDict.values()
        currentCutoff = numpy.percentile(list(values),80)
    return removeTopPercentile(key, vocabDict, currentCutoff)

def removeTopPercentile25(key,vocabDict):
    global currentPercentile
    global currentCutoff
    if currentPercentile != 25:
        currentPercentile = 25
        values = vocabDict.values()
        currentCutoff = numpy.percentile(list(values),75)
    return removeTopPercentile(key, vocabDict, currentCutoff)

def removeTopPercentile(key, vocabDict, cutoff):
    return vocabDict[key] > cutoff