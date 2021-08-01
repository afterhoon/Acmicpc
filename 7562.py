## 나이트의 이동
## https://www.acmicpc.net/problem/7562

from collections import deque

def knight(bx, by, ex, ey):
    queue = deque()
    queue.append([bx, by])
    board[bx][by] = 1
    # 해당 칸에서 나이트가 움직일수 있는 경우의 수를 찾은뒤
    # 나이트가 이동한 칸에서 다시 움직일 수 있는 경우 찾음 (이를 반복)
    while queue:
        a, b = queue.popleft()
        # 나이트가 이동하다가 목적좌표에 도달하면 출력하고 종료
        if a == ex and b == ey:
            print(board[ex][ey] - 1)
            return
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            # 나이트를 이동시킨 위치가 체스판 위이고 첫 도착이면 출발지점의 횟수+1을
            # 해당 좌표에 입력해주고 큐에 좌표를 추가해준다
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                queue.append([nx, ny])
                board[nx][ny] = board[a][b] + 1

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

T = int(input())
for t in range(T):
    l = int(input())
    bx, by = map(int, input().split())
    ex, ey = map(int, input().split())
    board = [[0 for i in range(l)] for j in range(l)]

    knight(bx, by, ex, ey)