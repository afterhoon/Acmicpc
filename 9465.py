## 스티커
## https://www.acmicpc.net/problem/9465

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(2):
        arr.append(list(map(int, input().split())))

    # 각 스티커는 변이 맞닿아있으면 더할 수 없으므로 대각선으로 합한다
    # 시작하는 방법은 첫줄과 두번째줄 두가지 경우가 있다
    for i in range(1, n):
        if i == 1: 
            # 처음은 앞에 하나밖에 없으므로 바로 대각선에 있는 스티커의 숫자를 더해준다
            arr[0][i] += arr[1][i - 1]
            arr[1][i] += arr[0][i - 1]
        else:
            # 이후에는 두 열중에 더 큰것을 더한다
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])

    # 첫번째줄과 두번째줄의 경우에서 더 큰것을 답으로 택한다
    print(max(arr[0][n - 1], arr[1][n - 1]))
