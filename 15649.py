## N과 M(1)
## https://www.acmicpc.net/problem/15649

from itertools import permutations

n, m = map(int, input().split())
# 1~n 까지의 리스트 생성
arr = [(i+1) for i in range(n)]
# permutations() 함수로 순열생성
arr = list(permutations(arr, m))

for i in range(len(arr)):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()