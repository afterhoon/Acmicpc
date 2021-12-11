## 회전
## https://www.acmicpc.net/problem/23813

n = list(map(int, input()))
k = sum(n) # 회전하는 동안 각 자리는 모든 숫자를 거치게 된다
ans = 0
for i in range(len(n)):
    ans = ans * 10 + k # 각 자리에 모든 수의 합을 넣어준다
print(ans)