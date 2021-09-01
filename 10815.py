## 숫자 카드
## https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

# 시간제한 2초에 input이 a,b 최대 50만개 씩이므로 
# 실행시간을 줄이기 위해 a를 set으로 했다
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# b를 순회하면서 각 숫자가 a에 있는지 확인한 후 맞는 결과를 출력한다
for i in b:
    if i in a:
        print("1", end=" ")
    else:
        print("0", end=" ")
print()