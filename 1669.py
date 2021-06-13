## 멍멍이 쓰다듬기
## https://www.acmicpc.net/problem/1669

import math

## 키가 커지고 작아지는데는 1씩의 차이만 둘 수 있으므로 계단식으로 계산하는것을 알아낼 수 있다
## 원숭이와 개의 키 차이(dist)의 값이 정수의 제곱인 수일때 같아지는 일수는 제곱근*2 -1 이 된다
## 또한 각 제곱이 되는 수 사이에는 2일의 텀이 존재하며 그 경계는
## dist와 보다 작은 가장 가까운 제곱수+제곱근의 값보다 위인지 아래인지로 판별한다
x, y = map(int, input().split())
dist = y-x
dist_sq = math.sqrt(dist)
dist_sq_int = int(dist_sq)
if dist == 0:
    day = 0
elif dist_sq == dist_sq_int:
    day = dist_sq_int * 2 - 1
else:
    if dist <= pow(dist_sq_int, 2) + dist_sq_int:
        day = dist_sq_int * 2
    else:
        day = dist_sq_int * 2 + 1

print(day)