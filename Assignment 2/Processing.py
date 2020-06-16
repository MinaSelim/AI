def filterAndRemove(vocabDict, categoryDict):
    lstOfRemovedWords = []
    for key in vocabDict.keys():
        if filtrable(key):
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

def filtrable(key):
    return key.find("(") != -1 or key.find(")") != -1 or key.find(".") != -1 or key.find("?") != -1 or key.find("!") != -1 or key.find("“") != -1  or key.find("\"") != -1 or key.find(",") != -1 or key.find("$") != -1 or key.find("‘") != -1
