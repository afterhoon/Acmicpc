## 연산자 끼워넣기
## https://www.acmicpc.net/problem/14888
import sys

def operation(i, res, add, sub, mul, div):
    global max_, min_
    if i == N:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return
    else:
        if add:
            operation(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            operation(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            operation(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            operation(i+1, int(res/nums[i]), add, sub, mul, div-1)

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_, max_ = 1000000000, -1000000000

operation(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)
