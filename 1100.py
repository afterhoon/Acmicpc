## 하얀 칸
## https://www.acmicpc.net/problem/1100

# 체스판 리스트 생성 0:흰색 1:검은색
board = [[(i+j)%2 for i in range(8)] for j in range(8)]
cnt = 0

for i in range(8):
    temp = input()
    for j in range(8):
        # 각 열마다 흰색(0)인 부분에서 기물이 있으면(F) 카운트 상승
        if board[i][j] == 0 and temp[j]=='F':
            cnt += 1

print(cnt)
