## Baseball
## https://www.acmicpc.net/problem/10214

t = int(input())
for _ in range(t):
    y, k = 0, 0

    # 각각의 점수에 9회까지 점수를 더해준다
    for i in range(9):
        a, b = map(int, input().split())
        y += a
        k += b
    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    else:
        print("Draw")