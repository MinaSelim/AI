import Utility

def outputModelToFile(filename, vocabDict, categDict):
    dataToOutput = open(filename, "wt", encoding="utf-8")
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
    i = 0

    for key in vocabDict.keys():
        i += 1
        line = str(i) + " "
        line += key + " "
        line += str(categDict["story"].get(key)) + " "
        line += str(categDict["story"].get(key)/storySize) + " "

        line += str(categDict["ask_hn"].get(key)) + " "
        line += str(categDict["ask_hn"].get(key)/askSize) + " "

        line += str(categDict["show_hn"].get(key)) + " "
        line += str(categDict["show_hn"].get(key)/showSize) + " "
        
        line += str(categDict["poll"].get(key)) + " "
        line += str(categDict["poll"].get(key)/pollSize) + " " + "\n"
        dataToOutput.write(line)


        
