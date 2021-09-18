## 동전 0
## https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coin = []
amount = 0
for _ in range(n):
    coin.append(int(input()))

# 크기가 큰 동전부터 빼주면 최소한의 동전개수를 알수 있다
for i in range(n):
    amount += k // coin[n-i-1]
    k = k % coin[n-i-1]

print(amount)