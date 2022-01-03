## ZOAC 4
## https://www.acmicpc.net/problem/23971

h, w, n, m = map(int, input().split())
x, y = 0, 0
cnt = n
for i in range(h): # 첫 위치(0,0)에 사람을 두고 n, m만큼의 간격마다 사람을 둔다
    if cnt == n:
        cnt = 0
        y += 1
    else:
        cnt += 1

cnt = m
for i in range(w):
    if cnt == m:
        cnt = 0
        x += 1
    else:
        cnt += 1

print(x * y)