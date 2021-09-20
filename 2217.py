## 로프
## https://www.acmicpc.net/problem/2217

import sys
n = int(sys.stdin.readline().rstrip())
rope = []
for i in range(n):
    rope.append(int(sys.stdin.readline().rstrip()))
rope.sort()

# 로프를 여러개 사용할시 그중 (가장 약한 로프가 견디는 중량) * (그 이상의 로프의 수)
# 를 하면 각 로프를 포함한 최대로 견딜수 있는 중량을 알수 있다 
for i in range(n):
    rope[i] *= n-i
print(max(rope))