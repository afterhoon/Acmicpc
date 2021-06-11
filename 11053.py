## 가장 긴 증가하는 부분 수열
## https://www.acmicpc.net/problem/11053

import sys

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
cnt = [1 for i in range(N)]
ans = 0

## 각 원소의 앞을 확인해서 본인보다 낮은 숫자가 있으면
## 그 원소의 수열 길이에 +1을 해서(본인이 해당 숫자보다 하나 크므로) 
## 원래 가지고 있던 자신의 수열길이와 새로 생긴 값중 큰것을 자신의 수열 길이로 취한다
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)
    ans = max(ans, cnt[i])

print(ans)