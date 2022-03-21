## 전자레인지
## https://www.acmicpc.net/problem/10162

t = int(input())
timer = [300, 60, 10]
ans = [0, 0, 0]

if t % 10 == 0:
    for i in range(3):
        ans[i] = t // timer[i]
        t %= timer[i]
    print(" ".join(map(str, ans)))
else:
    print("-1")