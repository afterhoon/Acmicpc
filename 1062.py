## 가르침
## https://www.acmicpc.net/problem/1062
## 미완성

N, K = map(int, input().split())
arr = list(map(int, ord(input().split())))
apb = [0 for i in range(ord('z')-ord('a')+1)]
num = 0

print("N>> ", N)
print("K>> ", K)
for i in range(N):
    print(arr[i])

for i in range(N):
    apb = []
    cnt = 0
    for j in range(ord('a'), ord('z')):
        if arr[i] == j:
            apb[j-ord('a')] = 1
    for j in apb:
        if j == 1:
            cnt = cnt + 1
    if cnt <= K:
        num = num + 1

print(num)
