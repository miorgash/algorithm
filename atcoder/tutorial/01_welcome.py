import io
import sys

_INPUT = """\
1
10 100
hoge
"""
sys.stdin = io.StringIO(_INPUT)

# submission
a = int(input())
b, c = map(int, input().split(' '))
s = input()
print(f'{str(a+b+c)} {s}')
