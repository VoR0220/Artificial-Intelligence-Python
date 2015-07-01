#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Assign2.py
#  
# Class:     CSCI 490-B3
# Program:   Assignment 2
# Author:    RJ Catalano
# Z-number:  z1716703
# Date Due:  02/11/2015

# Purpose:   Read in file from command line, append .txt if not already there, assign points to each record line (treat upper and lower case letters the same), 
#			 print out score for each input record, lined up in neat order
# Execution: ./hw2.exe
#            

# Notes:     (optional) any special notes to your T.A. or other readers
#  
#  

import sys

#need to define a dictionary and somehow store values into it.

for eachArg in sys.argv:
    print (eachArg)
	
filename = sys.argv[1]
txt = ".txt"

if '.' not in filename:
    filename += txt

print ("File name is ", filename)


