## 패션왕
## https://www.acmicpc.net/problem/9375

from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    temp = []
    count = []
    ans = 1

    for i in range(n):
        name, kind = map(str, input().split())
        temp.append(kind) #temp에 종류에 문자열을 모두 입력해준다
    count = Counter(temp) #각 종류별로 몇개인지 Counter함수로 정리해준다

    for j in count: #입을 수 있는 경우의 수는 (각 의상의수 + 1) 들의 곱 - 1 이다
        ans *= count[j] + 1
    print(ans - 1)

