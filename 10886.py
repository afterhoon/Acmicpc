## 0 = not cute / 1 = cute
## https://www.acmicpc.net/problem/10886

n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()
cnt = 0
for i in range(n):
    if arr[i] == 0:
        continue
    cnt += 1

print("Junhee is cute!" if cnt*2 > len(arr) else "Junhee is not cute!")