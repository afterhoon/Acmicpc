## 윷놀이
## https://www.acmicpc.net/problem/2490

yut = ['E', 'A', 'B', 'C', 'D']
for i in range(3):
    arr = list(map(int, input().split()))
    # 배부분의 수를 세서 yut 리스트에 적힌 숫자를 출력
    print(yut[arr.count(0)])