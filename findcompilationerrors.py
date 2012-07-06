'''
Created on 04.July.2012

@author: SenthilKumar B
@Description: Searches for SQL Errors in the DDL Out file
'''
        
def findSQLStateErrors(v_filename,lstr_findString,blockSearch):
    file = open(v_filename)
    block =""
    #Scans till a new file is encountered. The lines are appended to a block of text
    #Once a new line is found the block is sought for SQL State Errors.
    if (blockSearch == 1):
        for content in file:
            if(content == "\n"):
                if (block.find(lstr_findString) > 0):
                    print (block)
                block = ""
            else:
                block+=content
        
            
        
findSQLStateErrors('C:\Eclipse\Projects\en.senthil.python.first\Training\SearchFile\SearchFile.txt','SQLSTATE',1)
