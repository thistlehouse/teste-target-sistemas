str = 'abcdefgh'

def reverseString(s):
    newStr = ''

    for i in range(len(s)-1, -1, -1):
        newStr = newStr+s[i]
    
    return newStr

newStr = reverseString(str)
print(newStr)