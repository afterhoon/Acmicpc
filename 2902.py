## KMP는 왜 KMP일까?
## https://www.acmicpc.net/problem/2902

s = input()

# 입력값의 첫글자에 하이픈(-) 다음 글자들을 이어붙인다
ans = s[0]
for i in range(len(s)):
    if s[i] == "-":
        ans += s[i+1]

print(ans)