## 돌게임 7
## https://www.acmicpc.net/problem/9661

'''
돌 게임은 두 명이서 즐기는 재밌는 게임이다.
탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 4x개 만큼 가져갈 수 있다. 
즉, 가능한 개수는 1, 4, 16, 64, ...개 이다. 4x개만큼 돌을 가져갈 수 있는 방법이 없는 사람이 게임을 지게 된다.
두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.
SK CY 
'''

n = int(input())
winner = 0
while n > 0:
    temp = 4
    while temp < n:
        temp *= 4
    n -= temp/4
    winner = 1 - winner
print("SK" if winner == 1 else "CY")