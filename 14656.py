## 조교는 새디스트야!!
## https://www.acmicpc.net/problem/14656

n = int(input())
s = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if s[i] != i+1:
        cnt += 1

print(cnt)