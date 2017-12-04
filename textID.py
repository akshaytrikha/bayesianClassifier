# textmodel.py
#
# TextModel project!
#
# names: A-Dawg, V-Bank, E-Money

from collections import defaultdict

"""
    Milestone methods:

    readTextFromFile(self, filename): should take in a filename (a string) and should return all of the text in that file as a single, very large string
    makeSentenceLengths(self, s): should use the text in the input string s to create the self.sentencelengths dictionary
    printAllDictionaries(self): should print out all five of self's dictionaries in full - for testing and checking how they are working...
    cleanString(self,s): should take in a string s and return a string with no punctuation and no upper-case letters
    makeWordLengths(self, s): should use the text in the input string s to create the self.wordlengths dictionary
    makeWords(self, s): should use the text in the input string s to create the self.words dictionary
    makeStems(self, s): should use the text in the input string s to create the self.stems dictionary
"""

# TODO: fix getWords to include case for non-sentence ending punctuation with two spaces in between it

input1 = ""
input2 = ""

endPunc = [".", "!", "?"] # sentence ending punctuation
nonEndPunc = [";", ":", ",", "-", "&", "–", "(", ")", "{", "}", "[", "]", "<", ">", '"', "'", "`", "”", "“"] # non-sentence ending punctuation
# different quotation mark types are included in list
# TODO: consider slanted single quotes
# TODO: consider the newline
suffixes = ["e", "es", "ly", "est", "ing", "s", "ism", "ist", "est", "ness", "ship", "sion", "tion", "ies", "ate", "ed", "en", "ize", "ise", "able", "ible", "al", "esque", "ful", "fully", "ic", "ical", "ious", "ous", "ish", "less", "y"]
suffixes.sort(key = len, reverse=True)
suffixCons = ["s"]
suffixVow2Cons = ["ing"]

def readText (fileName1):
    # reads text from a textFile
    currentFile = open(fileName1, "r")
    text = currentFile.readlines()
    currentFile.close()

    cleanList = list(map(lambda x: x.strip("\n"), text)) # removes the new line character, "\n" from text

    wordList = []
    for i in cleanList:
        wordList += i.split() # 

    return wordList # main list for algorithm

def getSentences (wordList):
    #  returns a list containing sentences
    if (wordList == []):
        return []
    else:
        sentenceList = []
        for i in range(len(wordList)):
            if (wordList[i][-1] in endPunc):
                sentenceList.append(wordList[:i + 1])
                print(sentenceList)
                return sentenceList + getSentences(wordList[i + 1:])
    
    return sentenceList

def makeSentenceDictionary (sentenceList):
    # returns a dictionary of sentences lengths and their frequencies
    sentenceDictionary = {}
    for i in sentenceList:
        if not (len(i) in list(sentenceDictionary.keys())):
            sentenceDictionary[len(i)] = 1
        else:
            sentenceDictionary[len(i)] += 1
    print("sentence dictionary")
    print(sentenceDictionary)
    print("")
    
    return sentenceDictionary

def getWords (wordList):
    # returns a list containing words (with no punctuation)
    for i in range(len(wordList)): # to clean list of all puntuation
        if wordList[i] in nonEndPunc or wordList[i] in endPunc:
            del wordList[i]
        elif wordList[i][-1] in nonEndPunc or wordList[i][-1] in endPunc:
            if len(wordList[i]) >= 2: # to avoid a index out of bounds error
                if wordList[i][-2] in nonEndPunc or wordList[i][-2] in endPunc: 
                    wordList[i] = wordList[i][:-2]
                else:
                    wordList[i] = wordList[i][:-1]
            else:
                wordList[i] = wordList[i][:-1]
        elif wordList[i][0] in nonEndPunc or wordList[i][0] in endPunc:
            wordList[i] = wordList[i][1:]

    print("word list")
    print(wordList)
    print("")

    return wordList

def makeWordLengthDictionary (wordList):
    # returns a dictionary of word lengths and their frequencies
    wordLengthDictionary = {}
    for i in wordList:
        if not (len(i) in list(wordLengthDictionary.keys())):
            wordLengthDictionary[len(i)] = 1
        else:
            wordLengthDictionary[len(i)] += 1

    print("word length dict")
    print(wordLengthDictionary)
    print("")
    
    return wordLengthDictionary

def makeWordCountDictionary (wordList):
    # returns a dictionary of words and their frequencies
    wordCountDictionary = {}
    for i in wordList:
        if not (i in list(wordCountDictionary.keys())):
            wordCountDictionary[i] = 1
        else:
            wordCountDictionary[i] += 1

    print("word count dict")
    print(wordCountDictionary)
    print("")
    
    return wordCountDictionary

def getPunc (wordList):
    # returns a list containing all forms of punctuation found
    puncList = []
    for i in range(len(wordList)): # to clean list of all puntuation
        if wordList[i][-1] in nonEndPunc or wordList[i][-1] in endPunc:
            puncList.append(wordList[i][-1])

            if len(wordList[i]) >= 2: # to avoid a index out of bounds error
                if wordList[i][-2] in nonEndPunc or wordList[i][-2] in endPunc: 
                    puncList.append(wordList[i][-2])

        if wordList[i][0] in nonEndPunc or wordList[i][0] in endPunc:
            puncList.append(wordList[i][0])

    print("punctuation list")
    print(puncList)
    print("")

    return puncList

def makePuncCountDictionary (puncList):
    # returns a dictionary of punctuation marks and their frequencies
    puncCountDictionary = {}
    for i in puncList:
        if not (i in list(puncCountDictionary.keys())):
            puncCountDictionary[i] = 1
        else:
            puncCountDictionary[i] += 1

    print("punctuation count dict")
    print(puncCountDictionary)
    print("")
    
    return puncCountDictionary

    def getStems(wordList):
        # returns a list of all word stems found
        stemList = []
        for i in wordList:
            for j in suffixes:
                if j in i:
                    stemList.append(i[:-len(j)])
                    break
            stemList.append(i)        

        return stemList       

    def makeStemsDictionary (stemList):
        # returns a dictionary of stems and their frequencies
        stemsDictionary = {}
        for i in stemList:
            if not (i in list(stemsDictionary.keys())):
                stemsDictionary[i] = 1
            else:
                stemsDictionary[i] += 1

        return stemsDictionary




text1 = readText("testText.txt") # a wordList
sentencesText1 = getSentences(text1) # a sentenceList
puncs = getPunc(text1) # a puncList


justWords = getWords(text1) # a list of only words (no punctuation)
print("juuuuuuust words",justWords)
makeWordLengthDictionary(justWords) # dictionary of key = length of word, value = frequency
makeWordCountDictionary(justWords) # dictionary of key = word, value = frequency
makePuncCountDictionary(puncs) # dictionary of key = punctuation, value = frequency

makeSentenceDictionary(sentencesText1) # dictionary of key = length of sentences, value = frequency










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