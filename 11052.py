## 카드 구매하기
## https://www.acmicpc.net/problem/11052

n = int(input())
p = [0]
p += list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = p[1]
dp[2] = max(p[2], p[1]*2)

for i in range(3, n+1):
    dp[i] = p[i] 
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[n])