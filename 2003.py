## 수들의 합
## https://www.acmicpc.net/problem/2003

from collections import deque
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dq = deque()
cnt = 0
# 숫자를 순서대로 dq에 입력해넣고 합이 m 이상이면
# 맨 앞부터 차례대로 제거하며 m과 같도록 맞춰준다
# m과 같아지면 cnt를 1 올리고 m보다 작아지면 다음으로 진행한다
for el in arr:
    dq.append(el)
    if sum(dq) >= m:
        while sum(dq) > m:
            dq.popleft()
        if sum(dq) == m:
            cnt += 1

print(cnt)