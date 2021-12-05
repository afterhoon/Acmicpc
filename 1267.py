## 핸드폰 요금
## https://www.acmicpc.net/problem/1267

'''
영식 Y 30초당 10원
민식 M 60초당 15원
'''
n = int(input())
call = list(map(int, input().split()))
y = 0
m = 0
for i in range(n): # 0~n-1 까지 k 요금을 가지므로 몫에 +1을 해준다
    y += (call[i] // 30 + 1) * 10
    m += (call[i] // 60 + 1) * 15

if y < m:
    print("Y", y)
elif y > m:
    print("M", m)
else:
    print("Y M", y)