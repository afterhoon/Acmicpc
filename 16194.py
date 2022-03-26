## 카드 구매하기
## https://www.acmicpc.net/problem/16194

n = int(input())

p = [0] + list(map(int,input().split()))
card = [0 for _ in range(n+1)]


for i in range(1, n+1):
    for k in range(1, i+1):
        if card[i] == False :
            card[i] = card[i-k]+p[k]
        else :
            card[i] = min(card[i], card[i-k]+p[k])

print(card[n])