## 네 번째 점
## https://www.acmicpc.net/problem/3009

## x축과 y축은 각각 두쌍씩 값이 일치하므로 
## 각리스트에 중복되지않은 원소 하나를 남긴다
def func(arr, n):
    if n in arr:
        arr.remove(n)
    else:
        arr.append(n)

a = []
b = []
for i in range(3):
    n, m = map(int, input().split())
    func(a, n)
    func(b, m)
print(a[0], b[0]) 