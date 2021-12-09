## 체커
## https://www.acmicpc.net/problem/1090
# x
n = int(input())
checker = []

for _ in range(n):
    checker.append(list(map(int, input().split())))
w = max(c[0] for c in checker) - min(c[0] for c in checker) + 1
h = max(c[1] for c in checker) - min(c[1] for c in checker) + 1

print("w:", w, "h:", h)
board = [[0 for i in range(w)] for j in range(h)]
visited = [[0 for i in range(w)] for j in range(h)]

for chk in checker:
    x = chk[0] - min(c[0] for c in checker)
    y = chk[1] - min(c[1] for c in checker)
    print(x, y)
    for i in range(h):
        for j in range(w):
            board[i][j] += abs(x + y - i - j)


print(*checker)
for i in range(h):
    print(" ".join(map(str, board[i])))

