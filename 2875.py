## 대회 or 인턴
## https://www.acmicpc.net/problem/2875

n, m, k = map(int ,input().split())
team = 0
while n + m >= k and n >= 0 and m >= 0: # 조건이 만족하는동안 반복
    n -= 2
    m -= 1
    team += 1
print(team-1) # 마지막 반복은 조건을 충족못한 case 이므로 -1 