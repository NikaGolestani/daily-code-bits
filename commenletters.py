def common_letters(str1, str2):
    mylist1 =list(str1.upper())
    mylist2 =list(str2.upper())
    mylist1.sort()
    mylist2.sort()
    resultstr=''
    i=0
    j=0
    while True:
        if i>=len(str1) or j>=len(str2):
            break
        elif  mylist1[i]==mylist2[j]:
            resultstr+=mylist1[i]
            i+=1
            j+=1
        elif mylist1[i]<mylist2[j]:
            i+=1
        elif mylist1[i]>mylist2[j]:
            j+=1
    return len(resultstr)
print(common_letters("ABCD", "ACDF"))  
print(common_letters("AGGTAB", "GXTXAYB"))  
print(common_letters("ABCBDAB", "BDCAB"))  
print(common_letters("ABCD", "EFGH"))  
print(common_letters("", "XYZ"))  
print(common_letters("ABCD", ""))  
print(common_letters("", ""))  