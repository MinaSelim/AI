def listContains(arr, item):
    for data in arr:
        if data == item:
            return True

    return False

def countNumOfWordsInDict(dictionary):
    num = 0
    for key in dictionary.keys():
        num += dictionary[key]
    return num

def outputListToFile(lst, filename):
    dataToOutput = open(filename, "wt", encoding="utf-8")
    for data in lst:
        dataToOutput.write(data)
        dataToOutput.write("\n")
