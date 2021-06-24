## 스택
## https://www.acmicpc.net/problem/10828

import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    # 문자열을 split해서 앞부분은 명령어로 뒷부분은 push 명령에 쓸 숫자로 활용한다
    str = sys.stdin.readline().split()
    command = str[0]

    if command=="push":
        stack.append(str[1])
    elif command=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command=="size":
        print(len(stack))
    elif command=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    # stack의 top은 stack의 맨 뒷 원소를 출력하면 된다
    elif command=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])