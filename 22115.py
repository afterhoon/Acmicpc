## 창영이의 커피
## https://www.acmicpc.net/problem/22115
## 시간초과
n, k = map(int, input().split())
coffee = [0] + list(map(int, input().split()))
arr = [[0 for i in range(k+1)] for j in range(n+1)]
cnt = [[0 for i in range(k+1)] for j in range(n+1)]

for i in range(n+1):
    caffeine = coffee[i]
    for j in range(1, k+1):
        if j < caffeine:
            arr[i][j] = arr[i-1][j]
            cnt[i][j] = cnt[i-1][j]
        else:
            if caffeine + arr[i-1][j-caffeine] >= arr[i-1][j]:
                arr[i][j] = caffeine + arr[i-1][j-caffeine]
                if caffeine + arr[i-1][j-caffeine] > arr[i-1][j]:
                    cnt[i][j] = cnt[i-1][j-caffeine] + 1
                else:
                    cnt[i][j] = min(cnt[i-1][j-caffeine] + 1, cnt[i-1][j])
            else:
                arr[i][j] = arr[i-1][j]
                cnt[i][j] = cnt[i-1][j]

if arr[n][k] == k:
    print(cnt[n][k])
else:
    print("-1")