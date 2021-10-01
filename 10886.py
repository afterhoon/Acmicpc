## 덱
## https://www.acmicpc.net/problem/10866

from collections import deque
import sys

queue = deque() # 덱으로 생성해서 front, back의 push, pop을 처리한다
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    # 명령어가 명령, 숫자 의 조합이면
    # command[0]과 command[1]에 각각 할당된다
    # 명령만 있다면 command[0]만 할당된다
    command = list(sys.stdin.readline().split())

    if command[0] == "push_front":
        queue.appendleft(command[1])
    elif command[0] == "push_back":
        queue.append(command[1])
    elif command[0] == "pop_front":
        print("-1" if len(queue)==0 else queue.popleft())
    elif command[0] == "pop_back":
        print("-1" if len(queue)==0 else queue.pop())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print("1" if len(queue)==0 else "0")
    elif command[0] == "front":
        print("-1" if len(queue)==0 else queue[0])
    elif command[0] == "back":
        print("-1" if len(queue)==0 else queue[-1])
