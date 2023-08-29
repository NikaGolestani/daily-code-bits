def longest_common_prefix(arr):
    #convert strings to lists and uppers to lowers
    for i in range(len(arr)):
        arr[i]=list(arr[i].lower())
    resultStr=""
    #pointer which stops at different letter
    j=0
    while True:
        #j th letter of first word if our word does not have j th letter return 
        try:
            x=arr[0][j]
        except IndexError:
            return resultStr
        for i in arr:
            #search until its different then return the resultStr
            try:
                if i[j]!=x:
                    return resultStr
            except IndexError:
                return resultStr
        resultStr+=x
        j+=1
print(longest_common_prefix(["flower", "Fl", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))    # Output: ""
print(longest_common_prefix(["apple", "ape", "april"]))    # Output: "ap"