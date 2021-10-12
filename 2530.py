## 인공지능 시계
## https://www.acmicpc.net/problem/2530

a, b, c = map(int, input().split())
d = int(input())

# 시작 시간을 모두 초로 바꾸어주고 요리하는데 필요한 시간(d)를 더해준 뒤
# 다시 시:분:초 스타일로 변환해 주었다
time = (a * 60 + b) * 60 + c + d
h = time // (60 * 60)
m = (time - h * 60 * 60) // 60
s = time - (h * 60 * 60 + m * 60)
print(h % 24,m,s)