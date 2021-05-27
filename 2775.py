## 부녀회장이 될테야
## https://www.acmicpc.net/problem/2775

import sys
T = (int)(sys.stdin.readline())
for i in range(T):
    k = (int)(sys.stdin.readline())
    n = (int)(sys.stdin.readline())
    apt = [[0 for col in range(n)] for row in range(k+1)]

    ## 각 층의 1호를 1로 초기화
    for i in range(k+1):
        apt[i][0] = 1
    
    ## 0층의 각 호에 해당 호수만큼 값 부여
    for i in range(n):
        apt[0][i] = i+1

    ## 각 호의 인원수는 왼쪽 집과 아래층 집의 인원수의 합
    for i in range(1,k+1):
        for j in range(1,n):
            apt[i][j] = apt[i-1][j] + apt[i][j-1]
    print(apt[k][n-1])