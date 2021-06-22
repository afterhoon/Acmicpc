## 로또
## https://www.acmicpc.net/problem/6603

from itertools import combinations

while True:
    arr = list(map(str, input().split()))
    if arr[0]=='0':
        break

    # 집합에서 6개의 숫자를 고르는 경우의 수는 조합으로 구할수 있다 따라서 combinations 함수를 이용했다
    res = list(combinations(arr[1:], 6))
    for i in range(len(res)):
        print(" ".join(res[i]))
    print()
