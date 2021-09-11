def solution(board, aloc, bloc):
    answer = 0
    rx = [1, 0, 0, -1]
    ry = [0, -1, 1, 0]
    player = [aloc, bloc]
    turn = 0
    end = False

    while True:
        answer += 1
        turn = 1 - turn
        for i in range(4):
            tx = player[turn][0] + rx[i]
            ty = player[turn][1] + ry[i]
            end = True
            try:
                if board[tx][ty] == 1:
                    board[player[turn][0]][player[turn][1]] == 0
                    player[turn] = [tx, ty]
                    end = False
                    print("A" if turn==0 else "B", player[turn]) ########
                    break
            except:
                continue
        
        if end:
            break

    return answer

solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])