## 최댓값
## https://www.acmicpc.net/problem/2562

ans = 0
cnt = 0
for i in range(9):
    temp = int(input())
    if temp > ans:
        ans = temp
        cnt = i+1
print(ans)
print(cnt)