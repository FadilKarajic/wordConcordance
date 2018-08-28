"""
File:wordConcordance (Data Structures Project).py
Author: Fadil Karajic
Description: Program opens and reads a stop word file (excluded words) into a binary tree dictionary.
            Program then opens and reads a file, words are appended into a binary tree dictionary with
            the line number on which the word appears unless the word is in the dictionary of excluded
            words. Words are then printed to a file along with the lines on which they appear. Once
            the concordance file is created the user is able to search for words in the console."""
            


#imported dictionary
from binary_search_tree import BinarySearchTree
import sys #recursion error changed default limit

def welcomeMessage():
    print("Program is running and creating word concordance, this will take a moment...")
    
def getUserInput():
    print("\nWord concordance created!\n")
    userInput=input("Enter the word you want to search or type in ""q"" to quit: ")
    return userInput

def getStopWords():
    """Reads in the stop words (excluded words) into binary tree dictionary"""
    
    stopWordDictionary=BinarySearchTree()   #Binary Search Tree dictionary
    myFile=open("stop_words.txt",'r')       #Open file
    for word in myFile:                     #Read file, lowercase letters and remove punctuations
        word=word.lower().strip()
        stopWordDictionary[word]=None
    myFile.close()                          #Close file and return the dictionary
    return stopWordDictionary
    
def wordLineCount(stopWords):
    """Reads words from a file,splits and strips words at punctuations,
        and performs the count of lines"""
    
    myFile=open("WatchersOfTheSky.txt",'r')
    lineCount=1                               #keep track of lines on which words appear
    sortedWordList=[]
    wordCountDictionary=BinarySearchTree()    #Binary Search Tree dictionary
    
    for line in myFile:                       #Goes through text line by line
        wordList=line.split()                 #Split words
        for word in wordList:                              
            word=word.lower().strip(',[]\'''"-().?!:;*#')  #Lowercase and strip punctuations                            
            if word not in stopWords:         #If word not one of the stop words append it to dictionary
                if word in wordCountDictionary:            
                    wordCountDictionary[word].append(lineCount)
                else:
                    wordCountDictionary[word]=[lineCount]
                    sortedWordList.append(word)           
        lineCount+=1
    myFile.close()                            #Close file, sort list and return dictionary and the sorted list of words
    sortedWordList.sort()
    return wordCountDictionary,sortedWordList

    
def printCount(dictionary,sortedWordList):
    """Prints the words and occurances in the line to text file"""
    
    outputFileName="wordConcordance.txt"     #create file
    for word in sortedWordList:              #write the concordance dictionary to file
        concordance=word,dictionary[word]
        myFile=open(outputFileName,'a+')
        print(concordance, file=myFile)
        
def searchWord(userInput):
    """Prints search results to console"""

    inputFile=open("wordConcordance.txt","r") #open concordance file
    for line in inputFile.readlines():        #user input passed
        if userInput in line:                 #if user input matches any of the lines
            print(line)                       #print that line


def main():
    
    sys.setrecursionlimit(10000) #system default is 1000 need to set to 10000
    welcomeMessage()
    stopWords=getStopWords()
    wordCountDictionary,sortedWordList = wordLineCount(stopWords)
    dictionary=printCount(wordCountDictionary,sortedWordList) #printCount function call
    userInput=getUserInput()
    while userInput !="q":
        searchWord(userInput)
        userInput=input("Enter the word you want to search or type in ""q"" to quit: ")

        
main()
