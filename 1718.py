## 암호
## https://www.acmicpc.net/problem/1718

plain = list(input())
crypt = list(input())
clen = len(crypt)
ans = []
i = 0
for c in plain:
    tmp = ord(c) - ord(crypt[i]) - 1
    if tmp < 0:
        tmp = 26 + tmp
    i = (i + 1) % clen
    ans.append(' ' if c == ' ' else chr(tmp + ord('a')))

print("".join(ans))