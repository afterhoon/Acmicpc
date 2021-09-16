## 좌표 정렬하기
## https://www.acmicpc.net/problem/11650

import sys
# 입력값이 최대 10만개이기 때문에 input() 사용시 시간초과로 실패
n = int(sys.stdin.readline().rstrip())
dot = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    dot.append([x,y])

dot.sort()
for p in dot:
    print(" ".join(map(str, p)))