## 모양 만들기
## https://www.acmicpc.net/problem/16932
## x
import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    dq = deque()
    dq.append((x,y))
    cnt = 1
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if arr[nx][ny]==1 and visited[nx][ny]==False:
                    visited[nx][ny] = True
                    cnt += 1
                    dq.append((nx,ny))
    return cnt

n, m = map(int, input().split())
arr = []
visited = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            temp = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                try:
                    if temp < visited[nx][ny]:
                        temp = visited[nx][ny]
                except:
                    temp = temp
            visited[i][j] = temp + 1

print()
for i in range(n):
    for j in range(m):
        print(visited[i][j], end=" ")
    print()
