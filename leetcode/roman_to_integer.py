import io
import sys
import re

table = '''\
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''
sys.stdin = io.StringIO(table)
pair = []
for i in range(6):
    k, v = re.sub(' +', ' ', input()).split(' ')
    pair.append((k, v))

print(pair)