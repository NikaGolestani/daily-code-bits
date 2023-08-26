def palindromeIndex(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        #checks if the half is same as reverse of other half
        if s[left] != s[right]:
            if s[left+1:right+1] == s[left+1:right+1][::-1]:
                return left
            if s[left:right] == s[left:right][::-1]:
                return right
        left += 1
        right -= 1
    
    return -1