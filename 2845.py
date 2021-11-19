## 파티가 끝나고 난 뒤
## https://www.acmicpc.net/problem/2845

l, p = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(5):
    arr[i] -= l*p
print(" ".join(map(str, arr)))