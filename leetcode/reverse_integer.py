# case 1
x = 123

# case 2
x = -123

# case 3
x = 1534236469

# submission
def reverse(x: int) -> int:
    UPPER_LIMIT = 2**31-1
    LOWER_LIMIT = -2**31

    coef = -1 if x < 0 else 1
    
    reversed = int(str(abs(x))[-1::-1]) * coef
    if LOWER_LIMIT <= reversed <= UPPER_LIMIT:
        res = reversed
    else:
        res = 0
    return res

reverse(x)