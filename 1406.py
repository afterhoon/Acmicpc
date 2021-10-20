## 에디터
## https://www.acmicpc.net/problem/1406
## x 시간초과
import sys

s = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline())

front = list(s)
back = []

for i in range(m):
    command = list(input().split())
    if command[0] == 'L' and front != []:
        back.append(front.pop())
    elif command[0] == 'D' and back != []:
        front.append(back.pop())
    elif command[0] == 'B' and front != []:
        front.pop()
    elif command[0] == 'P':
        front.append(command[1])

print("".join(front + list(reversed(back))))
