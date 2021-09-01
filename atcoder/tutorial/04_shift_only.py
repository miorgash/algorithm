import io
import sys
from time import sleep
_INPUT = '''\
6
382253568 723152896 37802240 379425024 404894721 -20
'''

sys.stdin = io.StringIO(_INPUT)

# submission
n = input()
nums = list(map(int, input().split(' ')))
i = 0

# for/while
while sum(map(lambda x: x % 2, nums)) == 0:
    nums = list(map(lambda x: x / 2, nums))
    i += 1

print(i)