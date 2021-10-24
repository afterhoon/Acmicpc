## 프린터 큐
## https://www.acmicpc.net/problem/1966

from collections import deque

t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))

    while queue:
        # 큐의 맨 앞이 가장 크면 출력하고 카운트를 1 올린다
        if queue[0] >= max(queue):
            queue.popleft()
            cnt += 1
            if m == 0:
                break
            m -= 1  # 맨 앞의 문서가 나갔으므로 모든 문서는 한칸 앞으로 간다

        # 중요도가 가장 크지 않다면 맨 뒤로 보낸다
        else:
            queue.append(queue.popleft())
            m = m-1 if m > 0 else len(queue)-1
    print(cnt)
