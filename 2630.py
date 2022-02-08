## 색종이 만들기
## https://www.acmicpc.net/problem/2630

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
res = []

def solution(x, y, n):
    color = paper[x][y]
  
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 정사각형 안의 모든 색이 같지 않다면 4등분한 뒤 다시 각각을 수행한다
            if color != paper[i][j]:
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return

    # 색이 모두 같다면 해당색의 카운트를 +1 해준다
    if color == 0:
        res.append(0)
    else:
        res.append(1)

solution(0, 0, n) # 함수 실행

# 결과값 출력
print(res.count(0))
print(res.count(1))