## 카드 정렬하기
## https://www.acmicpc.net/problem/1715
## x

n = int(input())
card = []
ans = 0
for _ in range(n):
    card.append(int(input()))
card.sort()
ans = card[0] * (n-1)
for i in range(1,n):
    ans += card[i] * (n-i)

print(ans)