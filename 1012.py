## 유기농 배추
## https://www.acmicpc.net/problem/1012

# 파이썬의 기본 재귀한도가 1000이라 그 이상으로 깊어질 경우
# recursion runtime error가 발생한다고 한다
# 그래서 sys.setrecursionlimit(100000) 을 입력해서 임의로
# 재귀 한도를 늘려주어 해결했다
# 참고: https://www.acmicpc.net/board/view/59436

import sys
sys.setrecursionlimit(100000)
t = int(sys.stdin.readline())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 해당 좌표의 상하좌우를 확인해서 최초로 발견한 인접 배추가 있으면 chk를 1로 바꾼다
# 인접한 배추를 발견할때마다 재귀적으로 수행한다
def worm(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= m or nx < 0 or ny >= n or ny < 0 or chk[nx][ny]:
            continue
        if cabbage[nx][ny] != 0:
            chk[nx][ny] = 1
            worm(nx, ny)

for _ in range(t):
    cnt = 0
    m, n, k = map(int, sys.stdin.readline().split())
    cabbage = [[0 for i in range(n)] for j in range(m)]
    chk = [[0 for i in range(n)]for j in range(m)]
    
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        cabbage[x][y] = 1

    for i in range(m):
        for j in range(n):
            if cabbage[i][j] == 1 and chk[i][j] == 0:
                chk[i][j] = 1
                cnt += 1
                worm(i, j)

    print(cnt)