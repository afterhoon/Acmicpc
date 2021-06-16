## 평범한 배낭
## https://www.acmicpc.net/problem/12865

import sys

n, k = map(int, input().split())
info = [[0, 0]]
bag = [[0 for i in range(k+1)] for j in range(n+1)]
for i in range(n):
    info.append(list(map(int, input().split())))

## 물건정보로 들어온 weight와 value값을 순서대로 비교한다
for i in range(1, n+1):
    weight = info[i][0]
    value = info[i][1]
    ## 각 물건마다 무게가 1일때부터 가방최대무게인 k까지 반복한다
    for j in range(1, k+1):
        ## 물건의 무게보다 낮은 케이스에서는 어차피 변화가 없으므로 위의 값을 그대로 가져와서 입력해준다
        if j < weight:
            bag[i][j] = bag[i-1][j]
        ## 해당물건 무게~ 가방 최대무게까지는 위의 값과 저번 물건에서의 가치값+해당물건의 가치를 더한값중에 큰것을 입력해준다
        else:
            bag[i][j] = max(value + bag[i-1][j-weight], bag[i-1][j])

print(bag[n][k])