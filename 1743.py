## 음식물 피하기
## https://www.acmicpc.net/problem/1743

import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    dq = deque()    # 큐의 기능을 활용할수 있는 deque를 이용한다
    dq.append((x,y))
    cnt = 1         # 최초로 발견하면 크기는 1부터 시작하게 된다
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            # dx와 dy를 이용해 각각 해당 좌표 상하좌우를 체크한다
            nx = dx[i] + x
            ny = dy[i] + y

            # 지정된 공간내에서 방문기록이 없고 쓰레기가 있는곳이 있다면 
            # cnt를 올리고 방문기록을 체크한뒤 다시 그 좌표기준으로 상하좌우를 살핀다
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if arr[nx][ny]==1 and visited[nx][ny]==False:
                    visited[nx][ny] = True
                    cnt += 1
                    dq.append((nx,ny))
    return cnt

n, m, k = map(int, sys.stdin.readline().split())
# 쓰레기의 위치를 기록하는 arr과 방문기록을 입력하는 visited를 선언한다
arr = [[0] * m for i in range(n)]
visited = [[False] * m for i in range(n)]
ans = 0

for i in range(k):
    r, c = map(int, sys.stdin.readline().split())
    arr[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        # 모든 위치중 쓰레기가 있으면서 방문기록이 없는 칸에서 크기를 구하고
        # 원래 가진 크기보다 크면 값을 바꾼다
        if arr[i][j]==1 and visited[i][j]==False:
            ans = max(ans, bfs(i, j))

print(ans)