## 첼시를 도와줘!
## https://www.acmicpc.net/problem/11098

n = int(input())
for _ in range(n):
    p = int(input())
    high = 0
    ans = ""
    for i in range(p):
        c, name = input().split()
        c = int(c)
        if high < c: #가장 큰 수를 찾을때마다 비용과 이름을 기억해둔다
            high = c
            ans = name;
    print(ans)
