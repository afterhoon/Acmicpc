## 사분면 고르기
## https://www.acmicpc.net/problem/14681
import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

loc = 0
def convertPM(n, k):
    if n > 0:
        return k
    else:
        return -k

loc = convertPM(x, 1) + convertPM(y, 2)

if loc == 3: print('1')
elif loc == 1: print('2')
elif loc == -3: print('3')
elif loc == -1: print('4')
