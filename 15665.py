## N과 M (11)
## https://www.acmicpc.net/problem/15665


def func(k):
    if k > m:
        print(" ".join(map(str, arr)))
        return
    for i in range(n):
        temp.append(arr[i])
        func(k+1)
        temp.pop()

n, m = map(int, input().split())
arr = sorted(list(set((map(int, input().split())))))
n = len(arr)
temp = []

func(1)

