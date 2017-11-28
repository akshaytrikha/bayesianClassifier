# textmodel.py
#
# TextModel project!
#
# names: A-Dawg, V-Bank, E-Money

from collections import defaultdict

input1 = ""
input2 = ""

endPunc = [".", "!", "?"] # sentence ending punctuation
nonEndPunc = [";", ":", ",", "-", "&", "–", "(", ")", "{", "}", "[", "]", "<", ">", '"', "'", "`", ] # non-sentence ending punctuation
# consider the newline 

def readText(fileName1):
    # reads text from a textFile
    currentFile = open(fileName1, "r")
    text = currentFile.readlines()
    currentFile.close()

    cleanList = list(map(lambda x: x.strip("\n"), text)) # removes the new line character, "\n" from text

    wordList = []
    for i in cleanList:
        wordList += i.split() # 

    # print(wordList)

    return wordList # main list for algorithm

def getSentences(wordList):
    #  returns a list containing sentences
    if (wordList == []):
        return []
    # elif (wordList[-1][-1] not in endPunc):
    else:
        sentenceList = []
        for i in range(len(wordList)):
            if (wordList[i][-1] in endPunc):
                sentenceList.append(wordList[:i + 1])
                print(sentenceList)
                return sentenceList + getSentences(wordList[i + 1:])

    # sentenceList = []
    # # wordListCopy = wordList

    # for i in range(len(wordList)):
    #     if wordList[i][-1] in endPunc:
    #         sentenceList.append(wordList[:i])
    #         wordList = wordList[i:]

    # print()
    # print(sentenceList)
    
    return sentenceList

dick = readText("testText.txt")
getSentences(dick)


TextModel1 = [ ]  # start with the empty list

words1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ words1 ]  # add that dictionary in...

wordlengths1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ wordlengths1 ]  # add that dictionary in...

stems1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ stems1 ]  # add that dictionary in...

sentencelengths1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ sentencelengths1 ]  # add that dictionary in...

# create one of your own...
# words1 = defaultdict( int )  # default dictionary for counting
# TextModel1 = TextModel1 + [ words1 ]  # add that dictionary in...

# a function to print all of the dictionaries in a TextModel1

def printAllDictionaries( TM ):
    """ a function to print all of the dictionaries in TM
        input: TM, a text model (a list of 5 or more dictionaries)
    """
    words = TM[0]
    wordlengths = TM[1]
    stems = TM[2]
    sentencelengths = TM[3]

    print("\nWords:\n", words)
    print("\nWord lengths:\n", wordlengths)
    print("\nStems:\n", stems)
    print("\nSentence lengths:\n", sentencelengths)
    print("\n\n")


# include other functions here...


# and, test things out here...
print("TextModel1:")
printAllDictionaries(TextModel1)