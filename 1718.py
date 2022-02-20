## 암호
## https://www.acmicpc.net/problem/1718

alp = [chr(i) for i in range(97, 97+26)]
print(alp)

plain = list(input())
crypt = list(input())
clen = len(crypt)
ans = []
i = 0
for c in plain:
    tmp = ord(c) - ord(crypt[i])
    if tmp < 0:
        tmp = 26 + tmp
    i = (i + 1) % clen
    if c != ' ':
        ans.append(chr(tmp + ord('a')))

print(ans)