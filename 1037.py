## 약수
## https://www.acmicpc.net/problem/1037

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 특정 숫자의 약수가 모두 주어졌을때 그 약수들이 정렬된 상태에서 
# 맨앞과 맨뒤에서 중앙까지의 각 숫자의 곱은 항상 해당 숫자가 나온다
print(arr[0]*arr[-1])