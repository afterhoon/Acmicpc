## Even or Odd?
## https://www.acmicpc.net/problem/18005

n = int(input())

if n % 2 == 1:
    s = 0
elif n // 2 % 2 == 0:
    s = 2
else:
    s = 1
    
print(s)