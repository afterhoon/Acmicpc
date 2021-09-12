## N과 M (3)
## https://www.acmicpc.net/problem/15651

n, m = map(int, input().split())
arr = []

def func(d, n, m):
    if d == m:
        print(" ".join(map(str, arr)))
        return
    # 재귀함수를 호출하여 길이가 3이상일때만 출력한다
    for i in range(n):
        arr.append(i+1)
        func(d+1, n, m)
        arr.pop()

func(0, n, m)