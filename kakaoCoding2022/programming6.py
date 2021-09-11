# board: 보드
# skill: [type(1:공격, 2:회복), (r1,c1), (r2,c2), damage]

def solution(board, skill):
    answer = 0

    for k in range(len(skill)):
        for i in range(skill[k][1],skill[k][3]+1):
            for j in range(skill[k][2],skill[k][4]+1):
                if skill[k][0] == 1:
                    board[i][j] -= skill[k][5]
                else:
                    board[i][j] += skill[k][5]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))