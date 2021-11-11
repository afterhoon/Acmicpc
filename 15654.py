## N과 M(5)
## https://www.acmicpc.net/problem/15654

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = []
visited = [False] * n

def func(depth):
    if depth == m: #정해진 길이에 도달하면 print
        print(' '.join(map(str, temp)))
        return
    for i in range(n):
        if not visited[i]: #방문 안한 숫자를 만나면 visited를 True로 바꾸고 재귀함수를 호출한다
            temp.append(arr[i])
            visited[i] = True
            func(depth + 1)
            visited[i] = False # 재귀함수 호출뒤에는 다음 순회를 위해 다시 False로 변경한다
            temp.pop()

func(0)