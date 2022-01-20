## N과 M (10)
## https://www.acmicpc.net/problem/15664

from itertools import combinations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 입력된 값을 정렬

arr = sorted(list(set(combinations(arr, m)))) # 조합중에서 중복을 제거하고 정렬한다

for i in arr:
    print(" ".join(map(str,i)))