## 저작권
## https://www.acmicpc.net/problem/2914

a, i = map(int, input().split())
print(a * (i-1) + 1) # 최소한을 구하기 위해서는 평균값에서 1을 빼준뒤 개수를 구하고 1을 더해준다