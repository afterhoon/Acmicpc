## 단어 뒤집기 2
## https://www.acmicpc.net/problem/17413
## x
S = list(map(str, input().split()))

for s in S:
    if s[0] == '<' and s[len(s)-1] == '>':
        print(s, end="")
    print(s[::-1], end=" ")