## 나는야 포켓몬 마스터 이다솜
## https://www.acmicpc.net/problem/1620

import sys
n, m = map(int, sys.stdin.readline().split())
name = {}
number = {}
num = 1

for i in range(n):
    temp = sys.stdin.readline().strip()
    # 딕셔너리를 이용해 서로 인덱스를 지정해준다
    name[num] = temp
    number[temp] = num
    num += 1

for i in range(m):
    temp = sys.stdin.readline().strip()
    # 입력받은 값이 int로 형변환이 되지 않으면(이름이면)
    # except로 출력한다
    try:
        print(name[int(temp)])
    except:
        print(number[temp])