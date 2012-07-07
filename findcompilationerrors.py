'''
Created on 04.July.2012

@author: SenthilKumar B

Time Complexity Analysis:
f(n) = 2 + n(1+2+1+1)
f(n) = 2 + 5n
f(n) = n

@Description: Searches for SQL Errors in the DDL Out file. Works fine for shorter blocks of text (<5 lines)

'''
import time
    
def findCompilationErrors(v_filename,lstr_findString):
    print ("Start time:" , time.time())
    file = open(v_filename)
    block =""
    #Scans till a new line is encountered. The lines are appended to a block of text
    #Once a new line is found the block is sought for SQL State Errors.
    for content in file:
        if(content == "\n"):
            if (block.find(lstr_findString) > 0):
                #print (block)
                block = ""
            block = ""
        else:
            block+=content
    
    print ("End time:" , time.time())
  
    
                   
findCompilationErrors('C:\Eclipse\Projects\en.senthil.python.first\Training\SearchFile\AverageCaseSearchFile.txt','SQL')
