## 나이순 정렬
## https://www.acmicpc.net/problem/10814

import sys

## N만큼의 리스트를 초기화한 뒤 나이, 이름 순으로 입력 받음
N = int(sys.stdin.readline())
member = [[0]*2 for i in range(N)]
for i in range(N):
    member[i] = list(input().split())
    member[i][0] = int(member[i][0])

## 나이를 기준으로 리스트 정렬
member.sort(key=lambda x: (x[0]))

for i in range(N):
    for j in range(2):
        print(member[i][j], end=" ")
    print()

