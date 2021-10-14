## 세탁소 사장 동혁
## https://www.acmicpc.net/problem/2720

change = [25, 10, 5, 1]
t = int(input())
for _ in range(t):
    c = int(input())
    # 각 동전의 크기에 맞게 차감해주면 된다
    for coin in change:
        print(c//coin, end=" ")
        c %= coin
    print()
