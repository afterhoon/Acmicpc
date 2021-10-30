## 그림
## https://www.acmicpc.net/problem/1926

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
paint = []
cnt = 0
size = 0

def bfs(y, x):
    dq = deque()
    dq.append((y,x))
    size = 1
    paint[y][x] = 0

    while dq:
        y, x = dq.popleft()
        for i in range(4):
            rx = dx[i] + x
            ry = dy[i] + y

            if 0 <= rx < m and 0 <= ry < n:
                if paint[ry][rx] == 1:
                    paint[ry][rx] = 0
                    size += 1
                    dq.append((ry, rx))
    return size # 그림의 size 리턴

for i in range(n):
    paint.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if paint[i][j] == 1:
            size = max(size, bfs(i,j)) # 그림을 발견하면 현재 가진 size와 비교해 더 큰것을 저장
            cnt += 1 # 그림을 찾을때마다 1씩 카운트 증가

print(cnt)
print(size)