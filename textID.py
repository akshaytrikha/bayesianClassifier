# textmodel.py
#
# TextModel project!
#
# names: A-Dawg, V-Bank, E-Money

from collections import defaultdict
import math

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
suffixes.sort(key = len, reverse = True)
suffixCons = ["s"]
suffixVow2Cons = ["ing"]

def readTextFromFile (fileName1):
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
                return sentenceList + getSentences(wordList[i + 1:])
    return sentenceList

# wordList = ["I", "am", "a", "penis.", "Violet", "is", "also", "a", "penis."]

# print(getSentences(wordList))

def makeSentenceLengths (sentenceList):
    # returns a dictionary of sentences lengths and their frequencies
    sentenceDictionary = {}
    for i in sentenceList:
        if not (len(i) in list(sentenceDictionary.keys())):
            sentenceDictionary[len(i)] = 1
        else:
            sentenceDictionary[len(i)] += 1
    
    return sentenceDictionary

# TODO: modify this getWords so that it doesn't mutate text
def getWords (wordList):
    # returns a list containing words (with no punctuation)
    for i in range(len(wordList)): # to clean list of all puntuation
        if wordList[i] in nonEndPunc or wordList[i] in endPunc: # to clean word if it is just punctuation
            del wordList[i]
        elif wordList[i][-1] in nonEndPunc or wordList[i][-1] in endPunc: # to clean end of word punctuation
            if len(wordList[i]) >= 2: # to avoid a index out of bounds error
                if wordList[i][-2] in nonEndPunc or wordList[i][-2] in endPunc: # to clean 2nd from last punctuation
                    wordList[i] = wordList[i][:-2]
                else:
                    wordList[i] = wordList[i][:-1]
            else:
                wordList[i] = wordList[i][:-1]
        elif wordList[i][0] in nonEndPunc or wordList[i][0] in endPunc:
            wordList[i] = wordList[i][1:]

    return wordList

def makeWordLengthDictionary (wordList):
    # returns a dictionary of word lengths and their frequencies
    wordLengthDictionary = {}
    for i in wordList:
        if not (len(i) in list(wordLengthDictionary.keys())):
            wordLengthDictionary[len(i)] = 1
        else:
            wordLengthDictionary[len(i)] += 1
    
    return wordLengthDictionary

def makeWordCountDictionary (wordList):
    # returns a dictionary of words and their frequencies
    wordCountDictionary = {}
    for i in wordList:
        if not (i in list(wordCountDictionary.keys())):
            wordCountDictionary[i] = 1
        else:
            wordCountDictionary[i] += 1
    
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

    return puncList

def makePuncCountDictionary (puncList):
    # returns a dictionary of punctuation marks and their frequencies
    puncCountDictionary = {}
    for i in puncList:
        if not (i in list(puncCountDictionary.keys())):
            puncCountDictionary[i] = 1
        else:
            puncCountDictionary[i] += 1
    
    return puncCountDictionary

def getStems(wordList):
    # returns a list of all word stems found
    stemList = []
    for i in wordList:
        for j in suffixes:
            l = len(j)
            if i[-l:] == j:
                stemList.append(i[:-l])
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

def normaliseDictionary (dictionary):
    # returns a normalised version (value = between 0 and 1) of any input dictionary
    counts = sum(list(dictionary.values()))
    for i in list(dictionary.keys()):
        dictionary[i] = dictionary[i]/counts
    
    return dictionary

def buildTextModel(fileName):
    """ Calls dictionary building functions to create 5 dictionaries for a given text file.
        Returns the dictionaries in a list. 
    """

    text = readTextFromFile(fileName) # a wordList
    sentences = getSentences(text) # a sentenceList
    puncs = getPunc(text) # a puncList
    justWords = getWords(text) # a list of only words (no punctuation), MODIFIES TEXT SO THAT IT HAS NO PUNCTUATION
    stems = getStems(justWords)

    wordLength = makeWordLengthDictionary(justWords) # dictionary of key = length of word, value = frequency
    wordCount = makeWordCountDictionary(justWords) # dictionary of key = word, value = frequency
    punctuation = makePuncCountDictionary(puncs) # dictionary of key = punctuation, value = frequency
    sentenceLength = makeSentenceLengths(sentences) # dictionary of key = length of sentences, value = frequency
    stemsDictionary = makeStemsDictionary(stems) # dictionary of key = stem, value = frequency

    return [wordCount, wordLength, stemsDictionary, sentenceLength, punctuation]

def normaliseModel (TM):
    # normalises all dictionaries in textModel
    outputTextModel = []
    for i in TM:
        outputTextModel.append(normaliseDictionary(i))
    
    return outputTextModel

def smallestValue (dictionary1, dictionary2):
    # returns the smallest value between both dictionary1 and dictionary2
    min1 = min(dictionary1.values())
    min2 = min(dictionary2.values())
    return min(min1, min2)

def compareDictionaries (unknownDictionary, dictionary1, dictionary2):
    minvalue = smallestValue(dictionary1, dictionary2)
    minvalue = 0.001

    probability1 = 1
    for i in unknownDictionary:
        if i in dictionary1.keys(): 
            probability1 *= dictionary1[i]
        else:
            probability1 *= minvalue/2
    
    probability2 = 1
    for i in unknownDictionary:
        if i in dictionary2.keys(): 
            probability2 *= dictionary2[i]
        else:
            probability2 *= minvalue/2

    return [math.log(probability1), math.log(probability2)]

# TODO: change TM to textModel
# a function to print all of the dictionaries in a TextModel1
def printAllDictionaries( TM ):
    """ a function to print all of the dictionaries in TM
        input: TM, a text model (a list of 5 or more dictionaries)
    """
    words = TM[0]
    wordlengths = TM[1]
    stems = TM[2]
    sentencelengths = TM[3]
    punctuation = TM[4]

    print("\nWords:\n", words)
    print("\nWord lengths:\n", wordlengths)
    print("\nStems:\n", stems)
    print("\nSentence lengths:\n", sentencelengths)
    print("\nPunctuation:\n", punctuation)
    # print("\nNormalised Words:\n", TM[5])
    print("\n\n")

# and, test things out here...
TextModel1 = buildTextModel("testText1.txt") 
print("TextModel1:")
printAllDictionaries(TextModel1)
normalModel1 = normaliseModel(TextModel1)
printAllDictionaries(normalModel1)

TextModel2 = buildTextModel("testText2.txt") 
print("TextModel2:")
printAllDictionaries(TextModel2)
normalModel2 = normaliseModel(TextModel2)
printAllDictionaries(normalModel2)

TextModel3 = buildTextModel("testText3.txt") 
print("TextModel3:")
printAllDictionaries(TextModel3)
normalModel3 = normaliseModel(TextModel3)
printAllDictionaries(normalModel3)

minValue = smallestValue(normalModel2[0], normalModel3[0])
compareDictionaries(normalModel1[0], normalModel2[0], normalModel3[0])