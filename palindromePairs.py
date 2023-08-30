def palindrome_pairs(arr):
    mylist=[]
    pairs=[]
    #make all texts simple
    for i in arr:
        mylist.append(i.lower().strip())
    #check for all the possible results (0,1)(1,0),.......,(n,n)
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            #it cannot pair with itself
            if i!=j:
                #check if first of our string is same with end of any 
                if mylist[i][0]==mylist[j][-1]:
                    mystring=mylist[i]+mylist[j]
                    if check_palindrome(mystring):
                        pairs.append((i,j))
                
    return pairs
def check_palindrome(mystring):
    length=(len(mystring)+1)//2
    #if half is the reverse of the other hakf return true
    if mystring[0:length]==mystring[:-length-1:-1]:
        return True
    return False

# Test Case 1
input_words1 = ["abcd", "dcba", "lls ", "S", "sssll"]
output1 = palindrome_pairs(input_words1)
print(output1)  
# Expected Output: [(0, 1), (1, 0), (3, 2), (2, 4)]

# Test Case 2
input_words2 = ["bat", "tab", "rat", "tar"]
output2 = palindrome_pairs(input_words2)
print(output2)  
# Expected Output: [(0, 1), (1, 0), (2, 3), (3, 2)]

# Test Case 3
input_words3 = ["a", "aa", "aaa"]
output3 = palindrome_pairs(input_words3)
print(output3)  
# Expected Output: [(0, 1), (1, 0), (1, 2), (2, 1),(0,2),(2,0)]

# Test Case 4
input_words4 = ["race", "car", "cara", "ecar"]
output4 = palindrome_pairs(input_words4)
print(output4)  
# Expected Output: [(0, 1), (0, 3), (3,0)]

# Test Case 5
input_words5 = ["abc", "def", "ghi"]
output5 = palindrome_pairs(input_words5)
print(output5)  
# Expected Output: []