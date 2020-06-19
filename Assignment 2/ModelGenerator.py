import Utility
import math


def outputModelToFile(filename, vocabDict, categDict, smoothingValue):
    dataToOutput = open(filename, "wt", encoding="utf-8")
    categSizes = dict()
    for key in categDict.keys():
        categSizes[key] = Utility.countNumOfWordsInDict(categDict[key])
    vocabSize = Utility.countNumOfWordsInDict(vocabDict)
    pollSize = Utility.countNumOfWordsInDict(categDict["poll"])
    showSize = Utility.countNumOfWordsInDict(categDict["show_hn"])
    askSize = Utility.countNumOfWordsInDict(categDict["ask_hn"])
    storySize = Utility.countNumOfWordsInDict(categDict["story"])
    i = 0

    for key in vocabDict.keys():
        i += 1
        line = str(i) + " "
        line += key + " "
        line += str(categDict["story"].get(key) - smoothingValue) + "  "
        line += str(categDict["story"].get(key)/storySize) + "  "

        line += str(categDict["ask_hn"].get(key) - smoothingValue) + "  "
        line += str(categDict["ask_hn"].get(key)/askSize) + "  "

        line += str(categDict["show_hn"].get(key) - smoothingValue) + "  "
        line += str(categDict["show_hn"].get(key)/showSize) + "  "
        
        line += str(categDict["poll"].get(key) - smoothingValue) + "  "
        line += str(categDict["poll"].get(key)/pollSize) + "  " + "\n"
        dataToOutput.write(line)


def outputBaysianClassification(fileName, testData, modelData,types,vocabDict, categDict ):
    i = 0
    success = 0
    outputFile = open(fileName, "wt", encoding="utf-8")
    
    categSizes = dict()
    for key in categDict.keys():
        categSizes[key] = Utility.countNumOfWordsInDict(categDict[key])
    vocabSize = Utility.countNumOfWordsInDict(vocabDict)
    pollSize = Utility.countNumOfWordsInDict(categDict["poll"])
    showSize = Utility.countNumOfWordsInDict(categDict["show_hn"])
    askSize = Utility.countNumOfWordsInDict(categDict["ask_hn"])
    storySize = Utility.countNumOfWordsInDict(categDict["story"])

    pPoll = pollSize/vocabSize
    pShow = showSize/vocabSize
    pAsk = askSize/vocabSize
    pStory = storySize/vocabSize   

    probabilities = [pStory, pAsk, pShow, pPoll]


    for data in testData:
        i += 1
        outStr = str(i) + "  "
        sentence = data[0]
        outStr += sentence + "  "
        actualType = data[1]
        outStr += actualType + "  "
        logValue = computeBaysian(sentence, modelData, probabilities)
        outStr += str(logValue[0]) + "  "
        outStr += str(logValue[1]) + "  "
        outStr += str(logValue[2]) + "  "
        outStr += str(logValue[3]) + "  "
        predictedType = types[logValue.index(max(logValue))]
        outStr += predictedType + "  "
        if predictedType==actualType: 
            outStr += "right"
            success += 1
        else: 
            outStr += "wrong"
        outStr+= "\n"
        outputFile.write(outStr)
    accuracy = success/i

    return (accuracy,len(vocabDict))
    
    


def computeBaysian(sentence, modelData, probabilities):
    words = sentence.split()
    logValue = [0,0,0,0]

    logValue[0] += math.log10(probabilities[0])
    logValue[1] += math.log10(probabilities[0])
    logValue[2] += math.log10(probabilities[0])
    logValue[3] += math.log10(probabilities[0])

    for word in words:
        
        if modelData.get(word) is None:
            continue
        
        logValue[0] += math.log10(float(modelData[word][3]))
        logValue[1] += math.log10(float(modelData[word][5]))
        logValue[2] += math.log10(float(modelData[word][7]))
        logValue[3] += math.log10(float(modelData[word][9]))
    return logValue