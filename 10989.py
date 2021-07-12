## 수 정렬하기3
## https://www.acmicpc.net/problem/10989

'''
# quick sort를 이용한 방법 (메모리초과로 실패)
import sys

def quick(arr):
    length = len(arr)
    if length <= 1:
        return arr
    
    pivot = arr[length // 2]
    left, right, mid = [], [], []

    for i in range(length):
        el = arr.pop()
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            mid.append(el)
    return quick(left) + mid + quick(right)

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr = quick(arr)
for el in arr:
    print(el)
'''

import sys

# 숫자가 0~10000 이므로 크기가 10000인 list를 0으로 채운다
n = int(sys.stdin.readline())
arr = [0] * 10000

# 입력받은 수의 인덱스를 1 증가시킨다
for i in range(n):
    arr[int(sys.stdin.readline())-1] += 1

# 인덱스 순으로 해당 크기만큼 숫자를 반복출력한다
# 정석적인 정렬방법은 아니지만 정렬되는 효과를 가져온다 
for i in range(10000):
    for j in range(arr[i]):
        print(i+1)