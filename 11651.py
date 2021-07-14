## 좌표 정렬하기
## https://www.acmicpc.net/problem/11651

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
# key를 설정해서 y축-x축 순으로 정렬한다
arr.sort(key=lambda arr: (arr[1], arr[0]))
for el in arr:
    print(el[0], el[1])