## 모음의 개수
## https://www.acmicpc.net/problem/10987

txt = input()
cnt = 0
moum = ['a', 'e', 'i', 'o', 'u']

# 문자열을 순회하며 모음리스트와 비교해 같은문자가 있으면 1씩 카운트를 증가시킨다
for i in range(len(txt)):
    if txt[i] in moum:
        cnt += 1

print(cnt)