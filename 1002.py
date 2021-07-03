## 터렛
## https://www.acmicpc.net/problem/1002

import math
t = int(input())
for i in range(t):
    x1, y1, dist1, x2, y2, dist2 = map(int, input().split())

    # 피타고라스 방정식으로 두 점 사이의 거리 distance를 구한다
    distance = math.sqrt(pow(abs(x2-x1), 2)+pow(abs(y2-y1), 2))
    # case1) 두 점이 같을 경우 - 서로 거리가 다르면 절대 만나지 않고 같으면 무한대이다
    if distance == 0:
        if dist1 == dist2:
            print("-1")
        else:
            print("0")
    # case2) distance가 dist1+dist2와 같으면 원과 원 사이에 점 하나가 인접해 있다고 볼수 있고
    #        dist1-dist2와 같으면 dist가 큰쪽인 작은쪽을 품어서 외곽이 인접해있다고 할수 있다
    elif distance == dist1 + dist2 or distance == abs(dist1 - dist2):
        print("1")
    # case3) 차와 합 사이에 해당하는 경우 두 원이 교차하여 2번 인접한다
    elif abs(dist1 - dist2) < distance < dist1 + dist2:
        print("2")
    else:
        print("0")

