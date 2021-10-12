## 수 정렬하기
## https://www.acmicpc.net/problem/2751
# 1) sorted() 함수 사용: 시간 초과
# 2) 퀵정렬 사용: recursion 에러
# 3) cache 없는 퀵정렬: 시간 초과

import sys

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot + 1, end)
    return arr

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr = quicksort(arr,0, n-1)
for el in arr:
    print(el)