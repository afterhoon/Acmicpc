## 
## https://www.acmicpc.net/problem/23037

from functools import reduce
import sys
print(reduce(lambda cur, acc: int(acc)**5 + cur, list(sys.stdin.readline().rstrip()), 0))