## 제로
## https://www.acmicpc.net/problem/10773

import sys

K = int(sys.stdin.readline())
arr = []

## 숫자를 차례대로 입력하면서 0이 입력되면 최근 입력된 숫자부터 하나씩 제거하므로
## 스택을 연상할 수 있다
for i in range(K):
    temp = int(sys.stdin.readline())
    if temp == 0:
        arr.pop()
    else:
        arr.append(temp)
        
print(sum(arr))