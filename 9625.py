## BABBA
## https://www.acmicpc.net/problem/9625

n = int(input())
a = 1
b = 0
for _ in range(n):
    # A는 B로 B는 BA로 되므로 각 개수만 바꿔준다
    a, b = b, a + b

print(a, b)

'''
* 시간 초과
n = int(input())
s = "A"
for _ in range(n):
    temp = ""
    for i in s:
        temp += ("B" if i == "A" else "BA")
    s = temp

print(s.count("A"), s.count("B"))
'''