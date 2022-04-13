## 안녕
## https://www.acmicpc.net/problem/1535

n = int(input())
life = [0] + list(map(int, input().split()))
pleasure = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if life[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-life[i]] + pleasure[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])