## 연산자 끼워넣기
## https://www.acmicpc.net/problem/14888
import sys
def operation(i, res, op):
    global max_, min_
    if (i >= N-1):
        max_ = max(res, max_)
        min_ = min(res, min_)
    else:
        if(op[0]>0): 
            op[0] = op[0] - 1
            operation(i+1, res+arr[i], op)
        if(op[1]>0):
            op[1] = op[1] - 1
            operation(i+1, res-arr[i], op)
        if(op[2]>0):
            op[2] = op[2] - 1
            operation(i+1, res*arr[i], op)
        if(op[3]>0):
            op[3] = op[3] - 1
            operation(i+1, res//arr[i], op)

N = int(sys.stdin.readline())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
operation(0, arr[0], op)

print(max_)
print(min_)
