## 과제 안 내신 분..?
## https://www.acmicpc.net/problem/5597

stu = []
for i in range(28):
    stu.append(int(input()))
stu.sort()
for i in range(1, 31):
    if i not in stu:
        print(i)