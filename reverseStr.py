def reversestring(str):
    result=""
    length=len(str)
    for i in range( length):
        result+=str[length-1-i]
    return result
print(reversestring("hello"))  # Should print "olleh"
print(reversestring("12345"))  # Should print "54321"
print(reversestring("python"))  # Should print "nohtyp"