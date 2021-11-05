## Fly me to the Alpha Centauri
## https://www.acmicpc.net/problem/1011

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    cnt = 0
    move = 1
    sum = 0
    while dist > sum:
        cnt += 1
        sum += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)