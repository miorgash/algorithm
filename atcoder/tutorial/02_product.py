import io
import sys

_INPUT = '''\
1 3
'''

sys.stdin = io.StringIO(_INPUT)

# submission
a, b = map(int, input().split(' '))

p = a * b

check = lambda x: 'Even' if x % 2 == 0 else 'Odd'

print(check(a * b))