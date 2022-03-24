## 국영수
## https://www.acmicpc.net/problem/10825

n = int(input())

arr = []
for i in range(n):
    arr.append(list(input().split()))

# 0:이름 1:국어 2:영어 3:수학 이므로 각 조건에 맞게 정렬되도록 한다
arr.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(str(arr[i][0]))