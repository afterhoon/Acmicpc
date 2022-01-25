## 접미사 배열
## https://www.acmicpc.net/problem/11656

s = str(input())
ss = []

for _ in s:
    ss.append(s)
    s = s[1:]
ss.sort()
for i in ss:
    print(i)