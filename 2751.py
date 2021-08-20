## 수 정렬하기
## https://www.acmicpc.net/problem/2751
# x 시간초과
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr)
for el in arr:
    print(el)