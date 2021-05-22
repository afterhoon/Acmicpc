## 빗물
## https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
arr = list(map(int, input().split()))
block = [[0 for col in range(W)] for row in range(H)]
sum = 0
left = -1

for i in range(H):
    for j in range(W):
        if arr[j] > i:
            block[i][j] = 1

for i in range(H):
    for j in range(W):
        if block[i][j] == 1:
            if left == -1:
                left = j
            else:
                sum = sum + (j - left - 1)
                left = j
    left = -1
print(sum)
