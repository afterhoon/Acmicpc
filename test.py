num, c = map(int, input().split())
pnum = list(map(int, str(num)))
cur = pnum[:]
digit = len(pnum)
goal = []
maxx = 0
change = 0
same = 0
for i in range(digit):
    for j in range(digit):
        if cur[i] == cur[j] and i != j:
            same = 1
    goal.append(max(pnum))
    pnum.remove(max(pnum)) 
answer = 0
if num < 10 or (num < 100 and num%10 == 0):
    answer = -1
else:
    while True:
        if cur == goal:
            if same == 0:
                cur[-1] = goal[-2]
                cur[-2] = goal[-1]
            change += 1
        else:
            i = 0
            t = 0
            maxed = goal[0]
            mlist = []
            clist = []
            mlocal = []
            for i in range(digit):
                if goal[i] != maxed:
                    if t > 0: break
                    else: maxed = goal[i]
                if goal[i] == maxed and cur[i]!=goal[i]:
                    clist.append(i)
                    mlist.append(cur[i])
                    maxx = goal[i]
                    t += 1
            for i in range(digit):
                if cur[i] == maxx and goal[i] != cur[i]:
                    mlocal.append(i)  
            if change + t > c:
                clist = clist[0:c-change]
                mlist = mlist[0:c-change]
            for i in clist:
                cur[i] = maxx
                cur[max(mlocal)] = min(mlist)
                mlocal.remove(max(mlocal))
                mlist.remove(min(mlist))
                change += 1
        if change == c:
        	break
    answer = 0
    for i in cur:
        answer = answer*10+i
print(answer)