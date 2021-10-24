## 가위 바위 보
## https://www.acmicpc.net/problem/8896
'''

풀이중

'''
t = int(input())
for _ in range(t):
    n = int(input())
    bot = []
    for i in range(n):
        bot.append([])
        bot[i] = list(input())
    for i in range(len(bot[0])):
        rsp = [0, 0, 0]
        for j in range(n):
            if bot[j][i] == 'R':
                rsp[0] += 1<<j
            elif bot[j][i] == 'S':
                rsp[1] += 1<<j
            elif bot[j][i] == 'P':
                rsp[2] += 1<<j
        print(i,">> ", rsp)

        if rsp not in [0]:
            print("draw")
        else:
            

