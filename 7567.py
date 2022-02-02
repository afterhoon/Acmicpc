## 그릇
## https://www.acmicpc.net/problem/7567

tray = list(input())
ans = 10 # 첫 접시는 10의 크기
for i in range(1, len(tray)):
    if tray[i] == tray[i-1]: # 같으면 5 추가
        ans += 5
    else: # 다르면 10 추가
        ans += 10
print(ans)