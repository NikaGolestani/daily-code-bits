
def lps(str):
    x= len(str)
    str.lower().strip() 
    #handle spacing and lower upper cases
    lenOfWord=x 
    while True:
        lenOfWord-=1    
        #dec the lenofword each time so we can search and find the longest first
        indexOfEnd=lenOfWord 
        #since we want to chck all possiblities for words with lenofword letters we start with first one [0:lenofword]
        indexOfStart=0
        while indexOfEnd<x: 
            #if indexofend==x it means we are out of range of the word so indexofend should stop when it reaches x
            if indexOfStart<=0: 
                #if l<=0 [indexOfEnd:l:-1] is going to be empty so we have to check l==0  like [indexOfEnd::-1]
                if str[indexOfStart:indexOfEnd+1]==str[indexOfEnd::-1]:
                    return str[indexOfStart:indexOfEnd+1]
            if str[indexOfStart:indexOfEnd+1]==str[indexOfEnd:indexOfStart-1:-1]: 
                #if we say [1:3] means [1,2] so to include 3 we have to add 1 ,from end to begining [3:1:-1] gives[3,2] so we have add -1
                return str[indexOfStart:indexOfEnd+1]
            indexOfEnd=indexOfEnd+1 
            #first one is [0,indexofend] so by increasing indexofend and indexofstart we shift the range if lenofword is 4 and x is 6 ==> [0:4],[1:5],[2:6]
            indexOfStart+=1
        
        
print(lps("babbabd"))