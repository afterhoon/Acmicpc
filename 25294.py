## 달팽이와 쿼리
## https://www.acmicpc.net/problem/25294

Q = int(input())
arrs = [[] for i in range(10000)]
for _ in range(Q):
    query = list(map(int, input().split()))
    arr = []

    if arrs[query[1]]:
        arr = arrs[query[1]]
    else:
        arr = [[0 for i in range(query[1])] for j in range(query[1])]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        cnt = 0
        rx, ry = 0, 0
        d = 0
        memo = 0
        while cnt < query[1]*query[1]:
            cnt += 1
            arr[ry][rx] = cnt
            if cnt == query[2]:
                memo = (ry+1, rx+1)
            rx += dx[d]
            ry += dy[d]
            if not (0 <= rx < query[1] and 0 <= ry < query[1]) or arr[ry][rx] != 0:
                rx -= dx[d]
                ry -= dy[d]
                d = (d + 1) % 4
                rx += dx[d]
                ry += dy[d]

    if query[0] == 1:
        print(arr[query[2]-1][query[3]-1])
    else:
        print(' '.join(map(str, memo)))
