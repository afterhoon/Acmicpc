## OX퀴즈
## https://www.acmicpc.net/problem/8958

for _ in range(int(input())):
    print(sum(list(map(lambda x: len(x)*(len(x)+1)//2, list(input().split('X'))))))