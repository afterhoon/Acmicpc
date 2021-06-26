## 추첨을 통해 커피를 받자
## https://www.acmicpc.net/problem/21866

max_score = [(i//2+1)*100 for i in range(9)]
score = list(map(int, input().split()))
sum = 0
for i in range(9):
    # 점수중 하나라도 최대점수를 초과하면 hacker를 출력하고 종료
    if score[i] > max_score[i]:
        print("hacker")
        exit()
    sum += score[i]

if sum >= 100:
    print("draw")
else:
    print("none")