## 폭죽쇼
## https://www.acmicpc.net/problem/1773
## python3로 제출시 시간초과, pypy3로 제출시 pass

import sys
n, c = map(int, sys.stdin.readline().split())
timeline = [False] * (c+1)
cnt = 0

# 폭죽을 쏠때마다 timeline에 기록하고 cnt를 1 올린다
# 다음 폭죽을 쏠때 timeline에 폭죽을 쏜 기록이 이미 있다면 그냥 넘어간다
for i in range(n):
    temp = int(sys.stdin.readline())
    for k in range(temp, c+1, temp):
        if not timeline[k]:
            timeline[k] = True
            cnt += 1
print(cnt)