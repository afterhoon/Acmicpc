## 소수의 연속합
## https://www.acmicpc.net/problem/1644

from collections import deque


n = int(input())

a = [False, False] + [True] * (n-1)
arr = []
sum = 0
ans = 0
k = 0

# 에라토스테네스의 체로 n까지의 소수를 저장한다
for i in range(2, n+1):
    if a[i]:
        arr.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

# 저장된 소수를 통해 연속합이 n이 되는 경우를 카운트 한다
for i in arr:
    # 소수를 sum에 더해주다가 n을 초과하면 n 이하가 될때까지
    # sum을 맨 앞 원소부터 빼준다
    sum += i
    while sum > n:
        sum -= arr[k]
        k += 1
    
    # sum과 n이 같다면 카운트를 1 올린다
    if sum == n:
        ans += 1

print(ans)