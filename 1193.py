## 분수찾기
## https://www.acmicpc.net/problem/1193

'''
1    1 1    1   2
2    1 2    2   3
3    2 1    2   3
4    3 1    3   4
5    2 2    3   4
6    1 3    3   4
7    1 4    4   5
8    2 3    4   5
9    3 2    4   5
0    4 1    4   5
1    5 1


10 * 2 = n(n+1)

'''

import sys
x = int(sys.stdin.readline())
cnt = 0
line = 0
# 입력된 수가 / 방향으로 이어지는 선중 몇번째 선인지 확인한다
# ex) 14의 경우 10 < 14 <= 15 이므로 5번째 선임
while line < x:
    cnt += 1
    line += cnt
# 해당 선에서 몇번째 수인지 알기 위해서 해당 선의 첫번째 번호 바로 전으로 이동한다
line -= cnt

# 홀수번째 선이면 아래에서 위로, 짝수번째면 위에서 아래로 진행되기 때문에
# 두 case로 나눠서 진행한다. 각 분자분모의 합은 cnt +1과 같다
if cnt%2 == 1:
    mo = x - line
    ja = cnt - mo + 1
else:
    ja = x - line
    mo = cnt - ja + 1

print("%d/%d" % (ja, mo))