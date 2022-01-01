## 차이를 최대로
## https://www.acmicpc.net/problem/10819

from itertools import permutations
n = int(input())
a = list(map(int, input().split()))

per = permutations(a) # 순열 생성
ans = 0
 
for p in per:
    diffSum = 0 # 각 순열 사이의 차이를 모두 더하는 diffSum
    for j in range(len(p)-1):
        diffSum += abs(p[j]-p[j+1])
    if diffSum > ans:
        ans = diffSum # 가장 큰 diffSum을 ans에 저장
 
print(ans)