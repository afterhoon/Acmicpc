## 영식이와 친구들
## https://www.acmicpc.net/problem/1592

n, m, l = map(int, input().split())
catch = [0 for i in range(n)]
maxCatch = 1
throw = 0
player = 0
while True:
    catch[player] += 1 #이전 플레이어가 던진 공을 현재 플레이어가 받는다
    maxCatch = maxCatch if maxCatch > catch[player] else catch[player]
    if maxCatch >= m: #m초과 유무를 확인하기 위해 maxCatch를 확인한다
        break

    throw += 1 #다음 플레이어에게 던진다
    #다음 플레이어는 현재 플레이어가 받은 횟수가 홀수냐 짝수냐에 따라 방향이 정해진다
    if catch[player] % 2 == 1:
        player = (player + l) % n
    else:
        player = (player - l) if (player - l) >= 0 else n + (player - l)

print(throw)