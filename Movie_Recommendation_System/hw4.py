#!/usr/bin/env python3
#hw4.py
#
#Class: CSCI 490-B3
#Program: Movie Similarity
#Author: RJ Catalano
#Z-number: z1716703
#Date Due: 03/06/2015
#Purpose: to load a movie matrix from a file, figure out who likes it, and what other movies they would also like via a Pearson R coefficient. 
#
#
# Execution: ./hw4.py [number] (must also contain movie files)

import sys
import statistics

def getKey(item):
    return item[0]

def pCalc (movMat, movNumber, n, reviewers):
      
    xVals = [int(x) for i,x in enumerate(movMat[movNumber][1].split(';')) if i in reviewers]
    yVals = [int(x) for i,x in enumerate(movMat[n][1].split(';')) if i in reviewers]
    
    xi = sum(xVals) #get first movie values
    average1 = xi/len(reviewers)
    stdDev1 = statistics.stdev(xVals)
  
    yi = sum(yVals) #get second movie values
    average2 = yi/len(yVals)
    stdDev2 = statistics.stdev(yVals)

    r = 0 		#get r value
    newSum = [((x - average1) / stdDev1) * ((y-average2)/stdDev2) for x,y in zip(xVals, yVals)]
    r = (1/(len(reviewers)-1))*sum(newSum)    
    
    review = []		#append all values to the list
    review.append(r)
    review.append(average1)
    review.append(average2)
    review.append(stdDev1)
    review.append(stdDev2)
    review.append(n)
    review.append(len(reviewers))
         
    return review 


def compMov (movMat, movNumber, i):
    indexes1 = [i for i,x in enumerate(movMat[movNumber][1].split(';')) if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' ]
    indexes2 = [i for i,x in enumerate(movMat[i][1].split(';')) if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' ]

    compare = list(set(indexes1).intersection(indexes2))

    return compare

def printTop (movNames, movRev):
    print ("")
    print ('{0:<6}'.format("Compare Movie is:"), movNames[movRev[5]])
    print ('{0:<6}'.format("no. of common reviewers:"), movRev[6])
    print ('{0:<16}'.format("target average:"), movRev[1])
    print ('{0:<6}'.format("compare average:"), movRev[2])
    print ('{0:<16}'.format("target std: "), movRev[3])
    print ('{0:<16}'.format("compare std:"), movRev[4])
    print ('{0:<16}'.format("r: "), movRev[0])

comparisons = 0
movMat = []
movNumber = int(sys.argv[1]) - 1
movNames = []
summation = 0
rValues = 0
revMat = []
rev = []

with open("movie-names.txt", 'r', encoding="ISO-8859-1") as f:
    movNames = f.readlines()

with open("movie-matrix.txt", 'r', encoding="ISO-8859-1") as f:
    movMat = list(enumerate(f.readlines()))

nInput = str(movNumber)
lines = len(movMat)

while int(nInput) > int(lines) or int(nInput) < 0:
    nInput = input("Invalid. Please give a proper number to compare or type q or quit to exit:") - 1

while nInput != 'q' or nInput != 'quit' : #establish movNumber loop, from there get lines and columns
    columns = len(movMat[movNumber][1].split(';'))

    print("Movie number: Movie", movNames[movNumber]) #print information
    print ("*** No. of rows (movies) in matrix =", lines)
    print ("*** No. of columns (reviewers) =", columns)
    print ("Output shows r-value, movie no.|name, no. of ratings")
   

    for i in range(0,lines):
         reviewers = compMov(movMat, movNumber, i)
         if (len(reviewers) < 10):
              continue         
         rev = pCalc(movMat, movNumber, i, reviewers)
         revMat.append(rev)
         i += 1

    revMat=sorted(revMat, key=getKey, reverse=True)

    if (len(revMat) < 20):
         print("Insufficient Comparision Movies")
    else:
         for i in range(0,20):
             printTop(movNames, revMat[i])
    
    nInput = input("Please give a number to compare a movie or type 'quit':")
    if(nInput == 'q' or nInput == 'quit'):
        sys.exit()
    else:
        movNumber = int(nInput)

if (movNumber > str(lines)):
    print ("not a valid number...exiting")
    sys.exit()
