def find_largest_sum(arr):
    tempsum=arr[0]#on sign changes add to partialsum
    partialSum=[]
    j=1#pointer to the array
    while j<len(arr):#add numbers one by one until sign changes if sign changes add tempsum to partialsum 
        if arr[j]*arr[j-1]>0:
            tempsum+=arr[j]
        elif arr[j]*arr[j-1]<0:
            partialSum.append(tempsum)
            tempsum=arr[j] 
        j+=1
    partialSum.append(tempsum)
    #if begining or end is negative delete it
    if partialSum!=[] and partialSum[0]<0  :
        partialSum.pop(0)
    if  partialSum!=[] and partialSum[-1]<0 :
        partialSum.pop(-1)
        #add them part by part until 
    sum=0
    #add them together until the positive sum is less than absoulute value of next number in partialsum
    tempsum=[]
    for k in partialSum:
        if k>0:
            sum+=k
        elif  sum>=k*-1  :
            sum+=k
        elif  sum<k*-1  :
            tempsum.append(sum)
            sum=0
    tempsum.append(sum)
    return max(tempsum)
            
# Test Case 1
arr1 = [1, 2, -1, 3, 4, -1]
output1 = find_largest_sum(arr1)
print(output1)  # Expected: 9 (subarray [1, 2, -1, 3, 4])

# Test Case 2
arr2 = [-2, -3, 4, -1, -2, 1, 5, -3]
output2 = find_largest_sum(arr2)
print(output2)  # Expected: 7 (subarray [4, -1, -2, 1, 5])

# Test Case 3
arr3 = [1, -1, 2, -1, 3, -1]
output3 = find_largest_sum(arr3)
print(output3)  # Expected: 4 (subarray [2, -1, 3])

# Test Case 4
arr4 = [0, -2, -1, -3, -4]
output4 = find_largest_sum(arr4)
print(output4)  # Expected: 0 (empty subarray)

# Test Case 5
arr5 = [1, 2, 3, 4, 5]
output5 = find_largest_sum(arr5)
print(output5)  # Expected: 15 (subarray [1, 2, 3, 4, 5])
