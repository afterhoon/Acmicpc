#import time
#import sys
#start = time.time()

a = int(input())

b = [list(map(int, sys.stdin.readline().split(" "))) for i in range(a)]

c  = []

for i in b:
    d = sum(i[1:len(i)])/i[0]
    e = 0
    for j in range(1, len(i)):
        if i[j]>d:
            e+=1
    c.append(round(e/i[0], 3)*100)

for i in c:
    print(str(i)+("0"*(6-len(str(i))))+"%")
