## 수 이어 쓰기1
## https://www.acmicpc.net/problem/1748

import sys
n = sys.stdin.readline().rstrip()
length = len(n)
n = int(n)

# 숫자의 최대 자리수 아래 숫자들의 길이는 미리 알 수 있으므로 리스트에 기록해둔다
arr = [(10**(i+1)-10**i)*(i+1) for i in range(10)]

# 미리 기록해둔 최대 자리수 아래 길이의 합과 나머지숫자*숫자하나의 길이를 더한값을 출력한다
n -= 10**length
print((n+1)*length + sum(arr[:length]))