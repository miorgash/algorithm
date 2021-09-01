# case 1
x = 121

# case 2
x = -121

# submission
def isPalindrome(x: int) -> int:
    UPPER_LIMIT = 2**31-1
    LOWER_LIMIT = -2**31

    original = str(x)
    reversed = str(original)[-1::-1]
    return original == reversed

isPalindrome(x)