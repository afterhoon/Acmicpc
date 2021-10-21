## R2
## https://www.acmicpc.net/problem/3046

r1, s = map(int, input().split())
print(2*s - r1) 
# r2는 s + (r1과 s 사이의 거리)
# r2 = s + (s - r1) = 2*s - r1