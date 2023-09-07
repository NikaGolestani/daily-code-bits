#I'm not proud with this code it's just a challenge
def largestNumRecursive(arr):
    length=len(arr)
    #if our array is empty there is no largest
    if length==0:
        return None
    # if there is 1 item its the largest
    elif length==1:
        return arr[0]
    #if there is 2 items compare
    elif length==2:
        if arr[0]<arr[1]:
            return arr[1]
        else:
            return arr[0]
    #call it as many times that your items are 2 or less
    else:
        return largestNumRecursive([largestNumRecursive(arr[0:length//2]),largestNumRecursive(arr[length//2:])])
        
arr1 = [4, 7, 1, 9, 6]
print("Largest number in arr1:", largestNumRecursive(arr1))  # Should print 9

arr2 = [-2, -5, -1, -9, -6]
print("Largest number in arr2:", largestNumRecursive(arr2))  # Should print -1

arr3 = []
print("Largest number in arr3:", largestNumRecursive(arr3))  # Should print None for an empty array
    
