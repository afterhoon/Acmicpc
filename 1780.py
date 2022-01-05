## 종이의 개수
## https://www.acmicpc.net/problem/1780

n = int(input())
paper = []
result = [0, 0, 0]
for i in range(n):
    paper.append(list(map(int, input().split())))

def check(y, x, k): # 하나의 숫자로 통일된 종이인지 체크 (한가지일경우 True, 아니면 False)
    num = paper[y][x]
    for i in range(k):
        for j in range(k):
            if paper[y+i][x+j] != num:
                return False
    return True

def cut(y, x, k): # 통일된 숫자인지의 여부에 따라 종이를 자르는 함수
    if check(y, x, k): # 같은 숫자인지 체크
        result[paper[y][x] + 1] += 1 # 각각 result[0] -> -1 종이, result[1] -> 0 종이, result[2] -> 1의 종이 숫자를 입력
    else: # 아니라면 3x3으로 9등분한다
        for i in range(3):
            for j in range(3):
                cut(y + i * k//3, x + j * k//3, k//3) # 각 등분된 종이는 좌상단 기준으로 다시 자를지 여부를 체크한다
    return

cut(0, 0, n)
for i in range(3):
    print(result[i])