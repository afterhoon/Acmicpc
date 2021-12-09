## 달팽이
## https://www.acmicpc.net/problem/1913
# 재귀함수로 해결하면 recursive depth가 초과하여 에러 발생

n = int(input())
m = int(input())

dx = [1, 0, -1, 0] # 각각 우 하 좌 상
dy = [0, 1, 0, -1]

r = n // 2 # row
c = n // 2 # column
len = 0 # 한번에 들어갈 값의 길이
index = 1 # index

arr = [[0 for i in range(n)] for j in range(n)]

arr[r][c] = index
while True:
    for i in range(4): # 중앙을 기준으로 4개의 막대가 감싼 형태로 진행한다
        for j in range(len): # len만큼 같은 방향으로 진행한다
            index += 1
            r += dy[i]
            c += dx[i]
            arr[r][c] = index

    if r == c == 0: # (0, 0) 의 좌표로 오면 종료
        break

    r -= 1
    c -= 1
    len += 2 # len은 2씩 커진다

ans_x, ans_y = -1, -1 # m의 좌표 x, y 를 담기 위한 변수
for i in range(n):
    s = ""
    for j in range(n):
        s += str(arr[i][j]) + " "
        if arr[i][j] == m: # 출력을 위해 순회하는 중에 m을 찾으면 좌표를 기록한다
            ans_x, ans_y = i+1, j+1
    print(s[:-1]) # 문자열 s의 마지막에 있는 공백 삭제
print(ans_x, ans_y)