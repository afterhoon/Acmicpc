## 뒤집기
## https://www.acmicpc.net/problem/1439

#첫 원소와 비교해서 다를때마다 바로바로 뒤집어주면 최소횟수를 구할 수 있다

s = list(input())
m = 0 # m=0: 맨 첫원소와 같음 / m=1: 다름
cnt = 0

for i in range(1, len(s)):
    if s[i-1] != s[i]: #숫자가 바뀌는 경계 때만 처리해주면 된다
        if m == 0:
            cnt += 1
        m = 1 - m

print(cnt)
