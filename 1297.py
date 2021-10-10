## TV 크기
## https://www.acmicpc.net/problem/1297

d, h, w = map(int, input().split())
# 대각선 길이에 비율을 계산하여 출력
r = d / ((h ** 2 + w ** 2) ** 0.5)
print(int(h * r), int(w * r))