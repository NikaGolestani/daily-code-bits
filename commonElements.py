def common_elements(list1, list2):
    common_elements_arr=[]
    if len(list1)<len(list2):
        for i in list1:
            if i in list2:
                common_elements_arr.append(i)
                list2.remove(i)#handle the duplicates
    else:
        for i in list1:
            if i in list2:
                common_elements_arr.append(i)
                list2.remove(i)#handle the duplicates
    return common_elements_arr

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
# Expected Output: [3, 4, 5]
result = common_elements(list1, list2)
print(result)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Expected Output: []
result = common_elements(list1, list2)
print(result)

list1 = []
list2 = []
# Expected Output: []
result = common_elements(list1, list2)
print(result)

list1 = [1, 2, 3, 4, 5]
list2 = []
# Expected Output: []
result = common_elements(list1, list2)
print(result)

list1 = [1, 2, 3, 3, 4, 5]
list2 = [3, 4, 4, 5, 6, 7]
# Expected Output: [3, 4, 5]
result = common_elements(list1, list2)
print(result)