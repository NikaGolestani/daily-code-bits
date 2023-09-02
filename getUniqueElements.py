def get_unique_elements(elements):
    mylist=[]
    #make an empty list and add the elements one by one if it is not in the list
    for i in elements:
        if not i in mylist:
            mylist.append(i)
    return mylist

print(get_unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Should return [1, 2, 3, 4, 5]
print(get_unique_elements(['apple', 'banana', 'apple', 'cherry', 'banana'])) # Should return ['apple', 'banana', 'cherry']
            