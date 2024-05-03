from tkinter import *
from tkinter import ttk
import tkinter.filedialog

alphaNumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
sentence = []
bag_of_words = {}


def count(): #actual code for getting the counts of word/token or STEP 3
    numWords = 0

    for x in sentence:
        numWords += 1
 
        if (x in bag_of_words):
            bag_of_words[x] += 1

        else:
            bag_of_words[x] = 1
    write(numWords)


def clean(): #for Cleaning, STEP 2
    for x in range(0,len(sentence)):
        word = sentence[x].lower()
        newWord = ""
        for char in word:
            if (char in alphaNumeric):
                newWord = newWord + char
        sentence[x] = newWord
    sentence.sort()
    index = 0

    for x in range(len(sentence)):
        if (x == 0 and sentence[x] != ""):
            break
        elif (sentence[x] != ""):
            del sentence[0:x]
            break
    count()

def tokenize(whole): # FOr Tokenizing, STEP 1
    y = whole.split()
    for word in y:
        sentence.append(word)
    clean()
def write(numWords): #For Writing the output or answer
    keys_values = bag_of_words.items()

    fp = open("output.txt","w")
    fp.write("Dictionary Size: "+ str(len(bag_of_words))+"\n")
    fp.write("Total Number of Words: "+ str(numWords)+"\n")

    for x in keys_values:
        fp.write(str(x[0]) + " " + str(x[1])+"\n")
    fp.close()
def read(file): #for reading the input file
    fp = open(file,"r")
    whole = ""
    for line in fp:
        whole = whole + line
    fp.close()
    sentence.clear()
    bag_of_words.clear()
    tokenize(whole)
read("001.txt");

