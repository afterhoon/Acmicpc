## Sort 마스터 배지훈
## https://www.acmicpc.net/problem/17263

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
print(max(a)) # 오름차순의 맨 마지막수는 항상 가장 큰 수 이므로 정렬하지 않고 max를 사용했다