def binary_search(arr, target):
    #last index=end first index=start
    end=len(arr)-1
    start=0
    while True:
        #define the new middle
        mid=(start+end)//2
        #is the target equal to middle element if it is return it
        if arr[mid]==target:
            return mid
        #our list is a single element and our target is not middle one so return -1
        elif start==end:
            return -1
        #if it is larger than mid change the lower part to mid if it is smaller change the higher part to mid
        elif target<arr[mid]:
            end=mid-1
        elif target>arr[mid]:
            start=mid+1
            
#Test Cases
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(arr, target)
print(result)  # Should print 4 (the index of 5 in the list)

target = 11
result = binary_search(arr, target)
print(result)  # Should print -1 (11 is not in the list)