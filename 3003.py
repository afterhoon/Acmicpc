## 킹, 퀸, 룩, 비숍, 나이트, 폰
## https://www.acmicpc.net/problem/3003

chess_piece = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
ans = [0 for i in range(6)]

# 발견한 각 기물을 정량으로 빼준다
for i in range(6):
    ans[i] = chess_piece[i] - found[i]
print(" ".join(map(str, ans)))