## 별 찍기 - 19
## https://www.acmicpc.net/problem/10994

n = int(input())
stars = [[" " for i in range(1+(n-1)*4)] for j in range(1+(n-1)*4)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def drawStar(k):
    # 첫 좌표 설정
    rx = (n-k)*2
    ry = (n-k)*2

    # 1이 되면 마지막이므로 별을 하나 찍고 종료
    if k == 1:
        stars[(n-1)*2][(n-1)*2] = "*"
        return

    ## 각 변을 나눠서 공백을 별로 바꿔준다
    for i in range(4):
        for j in range((k-1)*4):
            stars[ry][rx] = "*"
            
            rx += dx[i]
            ry += dy[i]
    drawStar(k-1)


drawStar(n)
for i in range(1+(n-1)*4):
    for j in range(1+(n-1)*4):
        print(stars[i][j], end="")
    print()
