## 사칙연산
## https://www.acmicpc.net/problem/13420

t = int(input())
for _ in range(t):
    ans = 0
    arr = list(input().split())
    a = int(arr[0])
    b = int(arr[2])
    r = int(arr[4])

    # 각 사칙연산에 따른 계산을 수행한다
    if arr[1] == '+' and a+b == r:
        ans = 1
    elif arr[1] == '-' and a-b == r:
        ans = 1
    elif arr[1] == '*' and a*b == r:
        ans = 1
    elif arr[1] == '/' and a//b == r:
        ans = 1
    print("correct" if ans == 1 else "wrong answer")
