## 직사각형에서 탈출
## https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())
print(min(x,y,w-x,h-y)) # 상하좌우로 가장 짧은 거리를 출력