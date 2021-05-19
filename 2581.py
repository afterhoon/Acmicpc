## 소수 
## https://www.acmicpc.net/problem/2581
import sys

def prime(x):
    count = 0
    for i in range(x):
        if(x%(i+1)==0):
            count += 1
    if(count == 2):
        return 1
    else:
        return 0

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
min = 0
sum = 0
for i in range(M,N+1):
    if(prime(i)==1):
        if(min == 0):
            min = i
        sum = sum + i

if(sum == 0):
    print("-1")
else:
    print(sum)
    print(min)
