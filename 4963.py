## 섬의 개수
## https://www.acmicpc.net/problem/4963

# 각 좌표를 둘러싼 8개의 좌표를 체크하기 위해 추가해줄 dx, dy
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

# 너비 우선 탐색을 통해 해결해주었다
def bfs(i, j):
    land[i][j] = 0 # 체크한 땅은 중복 체크를 방지하기 위해 제거해둔다
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(8):
            rx = a + dx[k]
            ry = b + dy[k]

            # 새로운 land를 찾으면 해당 좌표를 기준으로 bfs를 수행하기 위해 queue에 저장해둔다
            if 0 <= rx < h and 0 <= ry < w and land[rx][ry] == 1:
                land[rx][ry] = 0
                queue.append([rx, ry])

while True:
    land = []
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    for i in range(h):
        land.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):

            if land[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)
