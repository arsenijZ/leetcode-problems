# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

def isPalindrome(x):
    if x < 0:
        return False
    elif x >= 0 and x < 10:
        return True
    
    str_x = str(x)
    left = 0
    right = len(str_x)

    for i in range(right//2+1):
        if(str_x[left+i] != str_x[right-i-1]):
            return False
    return True 

# test
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(1221))
print(isPalindrome(1213))