## 나는 너가 살아온 날을 알고 있다
## https://www.acmicpc.net/problem/2139

def isLeap(year): #윤년확인
    if year % 400 == 0:
        return True;
    elif year % 100 == 0:
        return False;
    elif year % 4 == 0:
        return True;
    return False;

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #각 달의 일수

while True:
    d, m, y = map(int, input().split())
    if d == m == y == 0: #0 0 0 이면 종료
        break
    month[2] = 29 if isLeap(y) else 28 #윤년이면 2월을 29일로, 아니면 28로 변경
    print(sum(month[:m]) + d) #해당월 전까지의 날짜의 합과 일 수를 더해준다