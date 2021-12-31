## 짝수 게임
## https://www.acmicpc.net/problem/23974
# x (recursive error)
n, k = map(int, input().split())
arr = []

def drawCoin(curr, pl, ygCoin, boardCoin):
    if curr >= boardCoin:
        if curr == boardCoin:
            if ygCoin % 2 == 0:
                arr.append(True)
        return
    
    for i in range(1,5):
        drawCoin(curr+i, 1-pl, ygCoin + (i if pl == 0 else 0), boardCoin)

drawCoin(n, 0, 0, k)
if True in arr:
    print("YG")
else:
    print("HS")