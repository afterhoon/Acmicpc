## 타일 채우기
## https://www.acmicpc.net/problem/15700

n, m = map(int, input().split())
print(n * m // 2)
''' 
n*m  result
2    1
3    1
4    2
5    2
6    3
7    3
8    4
 -> n*m // 2 == result 이다
'''