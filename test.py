import sys

A = int(sys.stdin.readline())
arr = list(sys.stdin.readline())
arr.pop()
sum = 0

for i in range(len(arr)):
    sum += int(arr[i])

print(sum)