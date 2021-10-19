## A -> B
## https://www.acmicpc.net/problem/16953

from collections import deque

a, b = map(int, input().split())
queue = deque([(a, 1)])
ans = -1

# bfs를 통해 해결한다
# 각 경우에 다음 과정도 수행할 수 있으면 queue에 추가해서 
# 더이상 진행 못할때까지 수행한다
while queue:
    i, cnt = queue.popleft()
    if i == b:
        ans = cnt
        break

    if i*2 <= b:
        queue.append((i*2, cnt+1))
    if i*10+1 <= b:
        queue.append((i*10+1, cnt+1))

print(ans)