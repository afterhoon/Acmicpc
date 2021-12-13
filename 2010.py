## 플러그
## https://www.acmicpc.net/problem/2010

import sys
input = sys.stdin.readline
n = int(input())
sum = 0
cnt = 0
for _ in range(n):
    sum += int(input())
    cnt += 1

print(sum - (cnt - 1)) # 꽂을 수 있는 플러그의 수는 모든 소켓수 - (멀티탭의 개수 - 1) 이다