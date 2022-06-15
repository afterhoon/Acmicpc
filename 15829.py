## Hashing
## https://www.acmicpc.net/problem/15829
# 부분성공

'''
from functools import reduce
n = int(input())
print(reduce(lambda cur, acc: cur + acc, list(map(lambda x, i: (ord(x)-ord('a')+1)*31**i, list(input()), [i for i in range(n)])), 0))
'''

n = int(input())
arr = list(input())
answer = 0
for i in range(n):
    answer = (answer<<5) - answer + ord(arr.pop()) - ord('a') + 1
print(answer)