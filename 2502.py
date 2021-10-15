## 떡 먹는 호랑이
## https://www.acmicpc.net/problem/2502

'''
첫날(a) 와 둘째날(b)를 통한 떡 개수 계산
1   a
2   b
3   a+b     1,1
4   a+2b    1,2
5   2a+3b   2,3
6   3a+5b   3,4
7   5a+8b   4,5
8   8a+13b  5,6
'''

d, k = map(int, input().split())

# 피보나치수열로 30일까지의 떡 개수 계산
arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]

x = arr[d-3]
y = arr[d-2]

for a in range(k//x + 1):
    for b in range(k//y + 1):
        temp = a*x + b*y
        if temp == k:
            print(a)
            print(b)
            exit()
        elif temp > k:
            break
        