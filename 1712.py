## 손익분기점
## https://www.acmicpc.net/problem/1712

import sys, math
a, b, c = map(int, sys.stdin.readline().split())

'''
# x가 판매량이라고 할때 다음과 같이 식을 정리할 수 있다
    1)  a + (b * x) < c * x
    2)  a  < (c - b) * x
    3)  x > a / (c - b) 
    
    즉, 식 a / (c - b)가 k라고 할 때
    k < x < k +1 이므로 int (a / (c - b)) + 1과 같다

    또한 식 k가 양수여야 하므로 b < c 여야 한다
'''


if b < c:
    print(int(a/(c-b))+1)
else:
    print("-1")