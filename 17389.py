## 보너스 점수
## https://www.acmicpc.net/problem/17389

n = int(input())
s = list(input())
bonus = 0
ans = 0
for i in range(len(s)):
    if s[i] == 'O': #O면 기본점수+보너스점수를 추가하고 보너스점수+1
        ans += i+1 + bonus
        bonus += 1
    else: #X면 초기화
        bonus = 0
print(ans)