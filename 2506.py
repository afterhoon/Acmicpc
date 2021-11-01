## 점수계산
## https://www.acmicpc.net/problem/2506

n = int(input())
arr = list(map(int, input().split()))
score = 1
ans = 0
for i in range(n):
    if arr[i] == 1: # 정답(1)이면 총점을 올리고 배점을 1 증가
        ans += score
        score += 1
    else: # 오답(0)이면 배점을 1로 초기화
        score = 1
print(ans)