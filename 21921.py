## 블로그
## https://www.acmicpc.net/problem/21921

N, X = map(int, input().split())
arr = list(map(int, input().split()))
tmp = 0
for i in range(X):
    tmp += arr[i]
max = tmp
count = 1
for i in range(N-X):
    tmp = tmp - arr[i] + arr[i+X]
    if max < tmp:
        max = tmp
        count = 1
    elif max == tmp:
        count += 1

if max == 0:
    print("SAD")
else:
    print(max)
    print(count)