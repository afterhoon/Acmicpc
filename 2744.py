## 대소문자 바꾸기
## https://www.acmicpc.net/problem/2744

s = list(input())
for i in range(len(s)):
    # 대소문자간의 아스키코드 간격 만큼 더하거나 빼준다
    s[i] = chr(ord(s[i])+32) if ord('A') <= ord(s[i]) <= ord('Z') else chr(ord(s[i])-32)

print("".join(s))