## 공바꾸기
## https://www.acmicpc.net/problem/10813

n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i] #i와 j를 swap한다
print(" ".join(map(str, arr[1:])))
