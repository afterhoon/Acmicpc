## 2xn 타일링
## https://www.acmicpc.net/problem/11726

'''
1   1   1
2   2   1 + 1
3   3   1 + 2
4   5   1 + 3 + 1
5   8   1 + 4 + 3
6   13   1 + 5 + 6 + 1
7   21   1 + 6 + 10 + 4
   ... 
9   55

(n-2) + (n-1) = (n)의 규칙을 보인다
ex) 8 + 13 = 21
'''

n = int(input())
a, b = 1, 2
for i in range(n-1):
    a, b = b, a+b
print(a % 10007)