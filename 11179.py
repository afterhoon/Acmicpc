## 2진수 뒤집기
## https://www.acmicpc.net/problem/11179

n = int(input())
b = list(format(n, 'b')) #입력받은 값 n을 2진수로 변환한다
ans = 0

while b:
    ans = (ans<<1) + int(b.pop()) #맨 뒤부터 이진수로 입력하며 쌓아간다

print(ans)