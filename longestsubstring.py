# Longest Substring Without Repeating Characters
def longestsubstring(str):
    return len(set(str))#set stores  variables without repeating

# Test Case 1
input_str1 = "abcabcbb"
output1 = longestsubstring(input_str1)
print(output1)  # Expected: 3

# Test Case 2
input_str2 = "bbbbb"
output2 = longestsubstring(input_str2)
print(output2)  # Expected: 1

# Test Case 3
input_str3 = "pwwkew"
output3 = longestsubstring(input_str3)
print(output3)  # Expected: 3

# Test Case 4
input_str4 = "abcdef"
output4 = longestsubstring(input_str4)
print(output4)  # Expected: 6

# Test Case 5
input_str5 = ""
output5 = longestsubstring(input_str5)
print(output5)