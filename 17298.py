## 오큰수
## https://www.acmicpc.net/problem/17298

import sys

n = int(sys.stdin.readline())
nge = list(map(int, sys.stdin.readline().split()))
temp = [0]
res = [-1] * n

for i in range(1,n):
    # 매 반복마다 인덱스를 스택에 추가하고 
    # 인덱스가 스택의 top보다 크면 스택의 top이 인덱스보다 작아질때까지 스택을 pop하고 그 값을 res에 넣어준다
    while temp and nge[i] > nge[temp[-1]]:
        value = temp.pop()
        res[value] = nge[i]
    temp.append(i)

print(' '.join(map(str, res)))