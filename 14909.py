## 양수 개수 세기
## https://www.acmicpc.net/problem/14909

arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i > 0:
        cnt += 1
print(cnt)