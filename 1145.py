## 적어도 대부분의 배수
## https://www.acmicpc.net/problem/1145

arr = list(map(int, input().split()))
n = min(arr)

while True:
    cnt = 0
    for i in range(5):
        if n % arr[i] == 0:
            cnt += 1
    if cnt > 2:
        print(n)
        break
    n += 1