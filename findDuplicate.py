def find_duplicates(arr):
    apearedBefore=[]#every number in array without duplicates
    duplicates=[]#every number that has a duplicate
    #for number i check if we had it previously if not add it to apearedBefore else check if it had a duplicate if not add it to duplicates
    for i in arr:
        if i in apearedBefore:
            if i not in duplicates:
                duplicates.append(i)
        else:
            apearedBefore.append(i)
    return duplicates
    
    
    return duplicates
print(find_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Should print [2, 4]
print(find_duplicates([1, 2, 3, 4, 5]))  # Should print []
print(find_duplicates([1, 1, 1, 1, 1]))  # Should print [1]
print(find_duplicates([]))  # Should print []