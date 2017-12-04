<<<<<<< HEAD
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

class Text:
    # TODO: fix getWords to include case for non-sentence ending punctuation with two spaces in between it


    endPunc = [".", "!", "?"] # sentence ending punctuation
    nonEndPunc = [";", ":", ",", "-", "&", "–", "(", ")", "{", "}", "[", "]", "<", ">", '"', "'", "`", "”", "“"] # non-sentence ending punctuation
    suffixes = ["e", "es", "ly", "est", "ing", "s", "ism", "ist", "est", "ness", "ship", "sion", "tion", "ies", "ate", "ed", "en", "ize", "ise", "able", "ible", "al", "esque", "ful", "fully", "ic", "ical", "ious", "ous", "ish", "less", "y"]
    suffixes.sort(key = len, reverse=True)
    suffixCons = ["s"]
    suffixVow2Cons = ["ing"]

    def __init__(self, fileName):
        
        self.fileName = fileName
        self.wordList = self.readTextFromFile()
        self.getWords()
        self.makeSentenceLengths(self.getSentences())
        self.makeWordLengthDictionary()
        self.makeWordCountDictionary()
        self.getPunc()
        self.makePuncCountDictionary()
        self.getStems()
        self.makeStemsDictionary()      

        # self.fileName = fileName
        # self.wordList = []
        # self.sentenceDictionary = {}
        # self.wordLengthDictionary = {}
        # self.wordCountDictionary = {}
        # self.puncList = []
        # self.puncCountDictionary = {}
        # self.stemList = []
        # self.stemsDictionary = {}

    # different quotation mark types are included in list
    # TODO: consider slanted single quotes
    # TODO: consider the newline 

    def readTextFromFile (self):
        # reads text from a textFile
        currentFile = open(self.fileName, "r")
        text = currentFile.readlines()
        currentFile.close()

        cleanList = list(map(lambda x: x.strip("\n"), text)) # removes the new line character, "\n" from text

        wordList = []
        for i in cleanList:
            wordList += i.split() # 

        self.wordList = wordList # main list for algorithm


    #TODO: make recursion work with OOP
    def getSentences (self):
        #  returns a list containing sentences
        if (self.wordList == []):
            return []
        else:
            sentenceList = []
            for i in range(len(self.wordList)):
                if (self.wordList[i][-1] in endPunc):
                    sentenceList.append(self.wordList[:i + 1])
                    print(sentenceList)
                    return sentenceList + getSentences(wordList[i + 1:])
        
        return sentenceList

    def makeSentenceLengths (self, sentenceList):
        # returns a dictionary of sentences lengths and their frequencies
        sentenceDictionary = {}
        for i in sentenceList:
            if not (len(i) in list(sentenceDictionary.keys())):
                sentenceDictionary[len(i)] = 1
            else:
                sentenceDictionary[len(i)] += 1
        
        self.sentenceDictionary = sentenceDictionary

    def getWords (self):
        # returns a list containing words (with no punctuation)
        for i in range(len(self.wordList)): # to clean list of all puntuation
            self.wordList[i] = self.wordList[i].lower()
            if self.wordList[i] in nonEndPunc or self.wordList[i] in endPunc:
                del wordList[i]
            elif self.wordList[i][-1] in nonEndPunc or self.wordList[i][-1] in endPunc:
                if len(self.wordList[i]) >= 2: # to avoid a index out of bounds error
                    if self.wordList[i][-2] in nonEndPunc or self.wordList[i][-2] in endPunc: 
                        self.wordList[i] = self.wordList[i][:-2]
                    else:
                        self.wordList[i] = self.wordList[i][:-1]
                else:
                    self.wordList[i] = self.wordList[i][:-1]
            elif self.wordList[i][0] in nonEndPunc or self.wordList[i][0] in endPunc:
                self.wordList[i] = self.wordList[i][1:]


    def makeWordLengthDictionary (self):
        # returns a dictionary of word lengths and their frequencies
        wordLengthDictionary = {}
        for i in self.wordList:
            if not (len(i) in list(wordLengthDictionary.keys())):
                wordLengthDictionary[len(i)] = 1
            else:
                wordLengthDictionary[len(i)] += 1

        self.wordLengthDictionary = wordLengthDictionary

    def makeWordCountDictionary (self):
        # returns a dictionary of words and their frequencies
        wordCountDictionary = {}
        for i in self.wordList:
            if not (i in list(wordCountDictionary.keys())):
                wordCountDictionary[i] = 1
            else:
                wordCountDictionary[i] += 1

        return wordCountDictionary

    def getPunc (self):
        # returns a list containing all punctuation 
        puncList = []
        for i in range(len(self.wordList)): # to clean list of all puntuation
            if self.wordList[i][-1] in nonEndPunc or self.wordList[i][-1] in endPunc:
                puncList.append(self.wordList[i][-1])

                if len(self.wordList[i]) >= 2: # to avoid a index out of bounds error
                    if self.wordList[i][-2] in nonEndPunc or self.wordList[i][-2] in endPunc: 
                        puncList.append(self.wordList[i][-2])

            if self.wordList[i][0] in nonEndPunc or self.wordList[i][0] in endPunc:
                puncList.append(self.wordList[i][0])

        self.puncList = puncList

    def makePuncCountDictionary (self):
        # returns a dictionary of punctuation marks and their frequencies
        puncCountDictionary = {}
        for i in self.puncList:
            if not (i in list(puncCountDictionary.keys())):
                puncCountDictionary[i] = 1
            else:
                puncCountDictionary[i] += 1

        self.puncCountDictionary = puncCountDictionary

    def getStems(self):
        # returns a list of all the stems found in a wordlist 
        stemList = []
        for i in self.wordList:
            for j in suffixes:
                if j in i:
                    stemList.append(i[:-len(j)])
                    break
            stemList.append(i)        

        self.stemList = stemList            

    def makeStemsDictionary (self):
        # returns a dictionary of stems and their frequencies
        stemsDictionary = {}
        for i in self.stemList:
            if not (i in list(stemsDictionary.keys())):
                stemsDictionary[i] = 1
            else:
                stemsDictionary[i] += 1

        self.stemsDictionary = stemsDictionary




    # def run(self):
    #     self.wordList = self.readTextFromFile()
    #     self.getWords()
    #     self.makeSentenceLengths(self.getSentences())
    #     self.makeWordLengthDictionary()
    #     self.makeWordCountDictionary()
    #     self.getPunc()
    #     self.makePuncCountDictionary()
    #     self.getStems()
    #     self.makeStemsDictionary()        
        
text1 = Text("testText.txt")
    
        
"""        
        text1 = readTextFromFile("testText.txt") # a wordList
        sentencesText1 = getSentences(text1) # a sentenceList
        puncs = getPunc(text1) # a puncList


        justWords = getWords(text1) # a list of only words (no punctuation)
        print("juuuuuuust words",justWords)
        makeWordLengthDictionary(justWords) # dictionary of key = length of word, value = frequency
        makeWordCountDictionary(justWords) # dictionary of key = word, value = frequency
        makePuncCountDictionary(puncs) # dictionary of key = punctuation, value = frequency

        makeSentenceLengths(sentencesText1) # dictionary of key = length of sentences, value = frequency
        makeStems(justWords) # list of all stems 
        makeStemsDictionary(makeStems(justWords))
"""




    # TextModel1 = [ ]  # start with the empty list

    # words1 = defaultdict( int )  # default dictionary for counting
    # TextModel1 = TextModel1 + [ words1 ]  # add that dictionary in...

    # wordlengths1 = defaultdict( int )  # default dictionary for counting
    # TextModel1 = TextModel1 + [ wordlengths1 ]  # add that dictionary in...

    # stems1 = defaultdict( int )  # default dictionary for counting
    # TextModel1 = TextModel1 + [ stems1 ]  # add that dictionary in...

    # sentencelengths1 = defaultdict( int )  # default dictionary for counting
    # TextModel1 = TextModel1 + [ sentencelengths1 ]  # add that dictionary in...


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
=======
# textmodel.py
#
# TextModel project!
#
# names: A-Dawg, V-Bank, E-Money

from collections import defaultdict

# TODO: fix getWords to include case for non-sentence ending punctuation with two spaces in between it

input1 = ""
input2 = ""

endPunc = [".", "!", "?"] # sentence ending punctuation
nonEndPunc = [";", ":", ",", "-", "&", "–", "(", ")", "{", "}", "[", "]", "<", ">", '"', "'", "`", "”", "“"] # non-sentence ending punctuation
# different quotation mark types are included in list
# TODO: consider slanted single quotes
# TODO: consider the newline 


def readText (fileName1):
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
    # returns a list containing 
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
>>>>>>> 3688d0ce1ba8b6218421aef9f706ffdf384eac0a
