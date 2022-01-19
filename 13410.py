## 거꾸로 구구단
## https://www.acmicpc.net/problem/13410

res = 0
n, k = map(int, input().split())
for i in range(1, k+1):
    res = max(res, int(str(n*i)[::-1])) # 문자열을 통해 역순으로 바꾼 뒤 저장된 값과 비교해서 큰 값으로 변경

print(res)