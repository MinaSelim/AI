from matplotlib import pyplot as plt

def displayStuff(bottomFreqRemov, topFreqRemov):
    fig, [axe1, axe2] = plt.subplots(2)
    botvoclst = []
    botperclst = []
    topvoclst = []
    topperclst = []
    for val in bottomFreqRemov:
        botperclst.append(val[0])
        botvoclst.append(val[1])
    
    for val in topFreqRemov:
        topperclst.append(val[0])
        topvoclst.append(val[1])
    


    axe1.plot(botvoclst, botperclst)
    axe1.set_title('Least frequent words removed')
    axe2.plot(topvoclst, topperclst)
    axe2.set_title('Most frequent words removed')
    plt.xlabel('Vocabulary Size')
    plt.ylabel('Accuracy')
    plt.subplots_adjust(hspace=0.3)
    plt.show()