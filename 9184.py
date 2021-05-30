## 신나는 함수 실행
## https://www.acmicpc.net/problem/9184

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20,20,20)

    ## 이미 경험했던 인자배열이면 mem리스트에 저장된 값으로 출력
    if mem[a][b][c]:
        return mem[a][b][c]

    ## 재귀함수를 리턴으로 끝내지 않고 mem리스트에 기록
    if a<b and b<c:
        mem[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return mem[a][b][c]
    else:
        mem[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return mem[a][b][c]
 
mem = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]
while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break

    print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))