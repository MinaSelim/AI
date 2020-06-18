import Utility

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
    return key.find("(") != -1 or key.find(")") != -1 or key.find(".") != -1 or key.find("?") != -1 or key.find("!") != -1 or key.find("“") != -1  or key.find("\"") != -1 or key.find(",") != -1 or key.find("$") != -1 or key.find("‘") != -1

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

#def removeTopPercentile(key, vocabDict,)