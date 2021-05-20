## 연산자 끼워넣기
## https://www.acmicpc.net/problem/14888
import sys

def operation(i, res, op):
    global max_, min_
    if i == N:
        max_ = max(res, max_)
        min_ = min(res, min_)

    else:
        if op[0]:
            op[0] = op[0] - 1
            operation(i+1, res+nums[i], op)
        if op[1]:
            op[1] = op[1] - 1
            operation(i+1, res-nums[i], op)
        if op[2]:
            op[2] = op[2] - 1
            operation(i+1, res*nums[i], op)
        if op[3]:
            op[3] = op[3] - 1
            operation(i+1, int(res/nums[i]), op)

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
min_, max_ = 1000000000, -1000000000

operation(1, nums[0], op)
print(max_)
print(min_)
