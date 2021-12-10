## 나이 계산하기
## https://www.acmicpc.net/problem/16199

born = list(map(int, input().split()))
date = list(map(int, input().split()))

y = date[0] - born[0] # 연나이

m = y - (1 if (date[1] - born[1])*100 + date[2] - born[2] < 0 else 0) 
# 만나이 = 연초를 기준으로 하는 연나이와 달리 만나이는 생일이 기준이므로 생일이 안지났으면 연나이-1

s = y + 1 # 세는나이 = 연나이 + 1

print(m)
print(s)
print(y)