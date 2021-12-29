## 거북이
## https://www.acmicpc.net/problem/2959

line = list(map(int, input().split()))
line.sort()
print(line[0] * line[2]) # 최대로 나오는 값은 가장 짧은 선과 2번째로 긴 선의 곱이다