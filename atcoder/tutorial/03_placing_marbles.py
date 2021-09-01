import io
import sys

_INPUT = '''\
100
'''

sys.stdin = io.StringIO(_INPUT)

# submission
print(sum(map(int, list(input()))))