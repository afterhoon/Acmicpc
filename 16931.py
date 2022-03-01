## 겉넓이 구하기
## https://www.acmicpc.net/problem/16931

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

top = n * m # 위와 아래의 면적

front = 0 # 앞, 뒤의 면적
for i in range(n):
    for j in range(m):
        this = arr[i][j]
        before = arr[i][j-1]
        if j == 0:
            front += this
        else:
            if before < this: # 이전 블럭보다 많다면 중간에 새로운 면의 형성되므로 그만큼 추가
                front += this - before

side = 0 # 좌, 우의 면적
for i in range(m):
    for j in range(n):
        this = arr[j][i]
        before = arr[j-1][i]
        if j == 0:
            side += this
        else:
            if before < this:
                side += this - before

print((top + front + side) * 2)