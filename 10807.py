## 개수 세기
## https://www.acmicpc.net/problem/10807

import sys
input = sys.stdin.readline
input()
arr = list(map(int, input().split()))
v = int(input())

print(arr.count(v))