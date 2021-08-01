## 블랙잭
## https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
card = list(map(int, input().split()))
ans = 0

# 완전 탐색을 수행한다
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                ans = max(ans, card[i] + card[j] + card[k])

print(ans)