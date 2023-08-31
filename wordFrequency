import re
def wordFrequency(string):
    #re.sub()===> del punc.   .lower===> case sensitivity    split===> turn it to list
    mylist=re.sub(r'[^\w\s]', ' ' , string).lower().split(" ")
    mylist.sort()
    result={}
    for i in range(0,len(mylist)-1):
        if mylist[i]=='':#space is not a word
            continue
        elif mylist[i] in result:
            result[mylist[i]] += 1#we have the word so just add it
        else:
            result[mylist[i]] = 1#add it to list with key of 1
    return  result


# Test Case 1: Basic Case
text1 = "This is a test. This is only a test."
result1 = wordFrequency(text1)
print(result1)
# Expected Output:
# {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}

# Test Case 2: Case Insensitivity
text2 = "Hello hello World world"
result2 = wordFrequency(text2)
print(result2)
# Expected Output:
# {'hello': 2, 'world': 2}

# Test Case 3: Punctuation
text3 = "Hello, world! How are you?"
result3 = wordFrequency(text3)
print(result3)
# Expected Output:
# {'hello': 1, 'world': 1, 'how': 1, 'are': 1, 'you': 1}

# Test Case 4: Empty Input
text4 = ""
result4 = wordFrequency(text4)
print(result4)
# Expected Output:
# {}

# Test Case 5: Long Text
text5 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
result5 = wordFrequency(text5)
print(result5)
# Expected Output:
# {'lorem': 1, 'ipsum': 1, 'dolor': 1, 'sit': 1, 'amet': 1, 'consectetur': 1, 'adipiscing': 1, 'elit': 1, 'sed': 1, 'do': 1, 'eiusmod': 1, 'tempor': 1, 'incididunt': 1, 'ut': 1, 'labore': 1, 'et': 1, 'dolore': 1, 'magna': 1, 'aliqua': 1}