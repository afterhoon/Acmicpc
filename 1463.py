## 1로 만들기
## https://www.acmicpc.net/problem/1463

import sys
n = int(sys.stdin.readline())

# 각 케이스에서 나누기 2를 했을경우 3을 했을경우를 찾기 위해 인덱스 0~3을 미리 설정해둔다
dp = [0, 0, 1, 1]

for i in range(4, n+1):
    # index 4부터 입력된 정수 n까지 횟수의 최솟값을 배열 dp에 입력하며 진행해준다
    dp.append(dp[i-1] + 1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])