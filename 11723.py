## 집합
## https://www.acmicpc.net/problem/11723

import sys
m = int(sys.stdin.readline())
# 공집합 list에 추가 제거하는 방식이 아니라 
# 있는 숫자는 1 없는 숫자는 0으로 체크하는 방식을 사용한다
s = [0 for i in range(21)]
for _ in range(m):
    line = list(map(str, sys.stdin.readline().split()))
    # 입력받은 line을 command와 num으로 나눈다
    # (all이나 empty일 경우에는 숫자가 입력 안되므로 생략)
    command = line[0]
    if not (command == "all" or command == "empty"):
        num = int(line[1])

    # 각 command에 맞는 동작을 실행한다
    if command == "add":
        s[num] = 1
    elif command == "remove":
        s[num] = 0
    elif command == "check":
        if s[num] == 1:
            print("1")
        else:
            print("0")
    elif command == "toggle":
        s[num] = 1 - s[num]
    elif command == "all":
        s = [1 for i in range(21)]
    elif command == "empty":
        s = [0 for i in range(21)]