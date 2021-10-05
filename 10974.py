## 모든 순열
## https://www.acmicpc.net/problem/10974

from itertools import permutations

n = int(input())

# itertools.permutations() 함수를 통해
# 1~n 까지의 수로 이루어진 순열 리스트를 만든다
arr = list(permutations([i+1 for i in range(n)]))

for i in arr:
    print(" ".join(map(str, i)))