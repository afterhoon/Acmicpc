## 괄호의 값
## https://www.acmicpc.net/problem/2504

import sys
bracket = sys.stdin.readline()
bracket = bracket[:-1]
stack = []
res = 0

for s in bracket:
    if s == ")":
        temp = 0
        while stack:
            top = stack.pop()
            if top == "(":
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2*temp)
                break
            elif top == "[":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)
    elif s == "]":
        temp = 0
        while stack:
            top = stack.pop()
            if top == "[":
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3*temp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)
    else:
        stack.append(s)

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        res = res + int(i)

print(res)
