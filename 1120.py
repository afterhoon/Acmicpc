## 문자열
## https://www.acmicpc.net/problem/1120

a, b = input().split()
al, bl = len(a), len(b)
ans = []
for i in range(bl - al + 1):
    cnt = 0
    for j in range(al):
        if a[j] != b[i + j]:
            cnt += 1
    ans.append(cnt)

print(min(ans))