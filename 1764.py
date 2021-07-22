## 듣보잡
## https://www.acmicpc.net/problem/1764

import sys
n, m = map(int, sys.stdin.readline().split())
listen = []
look = []
name = []

# 듣지못한 사람과 보지못한 사람을 각각 리스트에 입력
for i in range(n):
    listen.append(sys.stdin.readline().strip())
for i in range(m):
    look.append(sys.stdin.readline().strip())

# 두 리스트를 set으로 바꾸어 교집합을 구한뒤 다시 리스트로 변환하고 정렬
name = list(set(listen) & set(look))
name.sort()

len = len(name)
print(len)
for i in range(len):
    print(name[i])