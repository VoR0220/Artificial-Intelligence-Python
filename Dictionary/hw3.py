#!/usr/bin/env python3
#
#hw3.py
#
#Class: CSCI 490-B3
#Program: Zipf's Law
#Author: RJ Catalano
#Z-number: z1716703
#Date Due: 02/26/2015
#Purpose: Open a file, convert double hyphen to two spaces, replace all characters
#other than letters, the apostrophe and a single hyphen by a space. Use replace function
#of string, not a loop. Convert all of it to lower case. Make a table showing the frequency
#of each letter of the alphabet in the input. Create an empty dictionary. For each character in the input line,
#check to see whether that character already has an entry in the dictionary. If not add it with a value of 1. If yes, add 1 to the frequency.
#
#
# Execution: ./hw3.py whatever.txt > hw3out.txt

import sys

def printocc (d):
    columns = 5
    counter = 1
    for key,val in d:
        if (counter != 5):
            print(key, ':', val, end=" ")
            counter += 1
        else:
            print('\n')

#def gethyphens (str):
    #find out whether there are hyphens in string
    
     
    
#def getbchars (str):
    #search for number of bad chars
    #bchars = 0

#def cleanstring (str, list):
    #clean the string

list = ['\n', '!', '"', '#', '$', '%', '&', '(', ')', '*', ',',
'.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?',
'@', '[', ']', '_', '\xa0'] 
d = dict()
records = 0
chars = 0
cchars = 0
words = 0
total = 0
hlines = 0
	

with open(sys.argv[1], "rt", encoding="iso-8859-1") as in_file:
    for line in in_file:
         #search for hyphens, search for "bad chars"
         records += 1
         line.replace("--","  ")
         line.lower() 
         num_words = len(line.split())
         str1 = ''.join(list)
         if(records < 2):
             print (str1)
         for char in str1:
              #print (char)
              badchar = line.count(char)
              if (badchar > 1):
                   line.replace(char, " ")
                   print (line)
#              if (records < 20): 
#                  print (line)
#         if char in line: 
#            d[char] += 1
#         else:
#            d[char] = 1
         sorted(d)
         words += num_words
         chars += len(line)
      #   if (records < 5):
      #       print(line)

print("no. of arguments =", len(sys.argv))
print("arguments are:", str(sys.argv))
print("\n")
print("Records read:", records)
print("Characters read:", chars)
print("Characters counted:", cchars)
print("Words counted:", words)
print("Distinct characters:", len(d))
print("\n")
print("Lines with --", hlines)
print("Invalid chars", list)



