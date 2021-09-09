## 전자레인지
## https://www.acmicpc.net/problem/14470

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# 원래 고기의 온도가 영하라면 3부분으로 걸쳐 계산한다
if a < 0:
    print((-a)*c + d + b*e)
else:
    print((b-a)*e)