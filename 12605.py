## 단어순서 뒤집기
## https://www.acmicpc.net/problem/12605

n = int(input())
for i in range(n):
    s = list(input().split())
    print("Case #", i+1, ": ", sep="", end="")
    print(" ".join(reversed(s)))