## 문자열 집합
## https://www.acmicpc.net/problem/14425

n, m = map(int, input().split())
s = []
cnt = 0

for _ in range(n):
    s.append(input())

for _ in range(m):
    temp = input()
    if temp in s:
        cnt += 1

print(cnt)