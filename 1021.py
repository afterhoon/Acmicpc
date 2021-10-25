## 회전하는 큐
## https://www.acmicpc.net/problem/1021
# 시간초과

from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque([i+1 for i in range(n)])
cnt = 0
for i in range(m):
    idx = queue.index(arr[i])
    if idx < n-idx :
        while True:
            queue.append(queue.popleft())
            idx = idx - 1
            cnt += 1
            if idx == 0:
                break
    else:
        while True:
            queue.appendleft(queue.pop())
            idx = (idx + 1) % n
            cnt += 1
            if idx == 0:
                break
    queue.popleft()
    n -= 1

print(cnt)