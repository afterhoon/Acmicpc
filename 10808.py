## 알파벳 개수
## https://www.acmicpc.net/problem/10808

s = input()
alp = [0] * 26
for i in range(len(s)):
    alp[ord(s[i])-ord('a')] += 1
print(" ".join(map(str, alp)))