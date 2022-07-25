## import package
import regex as re # regex = regular expression -> package used for text processing

## open 'ABM.txt' file using "open" function

f = open('ABM.txt','r') # 'r' stands for "read only"
dat = f.read() # store data in 'dat' variable
f.close() # when use "open" function to open the file, you must close the file after using it


count = re.findall('Alabama', dat) # use 're' to find all the 'aAabama'
print(count) # this will retur n an array of ['Alabama', 'Alabama', ... ,'Alabama']
print(len(count)) # this will return the number of element of the 'count' array which is the number of 'Alabama' words in the main file
    
