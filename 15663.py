## N과 M(9)
## https://www.acmicpc.net/problem/15663
## 틀림
from itertools import permutations

n, m = map(int, input().split())
arr = list(map(str, input().split()))
per = list(set(permutations(arr, m)))
per.sort()

for i in range(len(per)):
    for j in range(m):
        print(per[i][j], end=' ')
    print()