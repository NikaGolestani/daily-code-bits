def is_anagram(str1,str2):
    #make sure the space and upper lower problems are out
    str1 = str1.lower().replace(" ", "")
    str2 = list(str2.lower().replace(" ", ""))
    #eliminates if the number of  char are not the same
    if len(str1)!=len(str2):
        return False
    #if we delete one char for every char in str1 if the chars are the same str2 should be empty by end of the loop
    for i in str1:
        try:
            str2.remove(i)
        except:
            return False
    return str2==[]

print(is_anagram("silent","listen "))