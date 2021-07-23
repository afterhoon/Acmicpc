## N과 M(9)
## https://www.acmicpc.net/problem/15663

from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 입력받은 숫자를 permutations() 함수로 수열을 만들고 per에 입력한 뒤
# set를 한번 거쳐서 중복을 제거하고 sort()로 정렬한다
per = list(set(permutations(arr, m)))
per.sort()

for i in range(len(per)):
    for j in range(len(per[i])):
        print(per[i][j], end=' ')
    print()