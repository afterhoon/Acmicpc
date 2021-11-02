input = __import__('sys').stdin.readline

n,b,u = map(int, input().split())
enemy = 0

def no_barrack(m1, m2, can_attack = 0, opt = False):
    cnt = 0
    while m1 > 0 and m2 > 0:
        if can_attack:
            m2 -= can_attack
            can_attack = 0
        else:
            m2 -= m1
        m1 -= m2
        cnt += 1
    if not opt:
        return m1 <= 0
    else:
        return m1 <= 0, cnt

for ans in range(1, 5011):
    b -= (n - enemy)
    if b <= 0:
        break
    enemy = u
    if b < n and not no_barrack(n, enemy, can_attack= n - b):
        break

if ans == 5010:
    print(-1)
else:
    flag, cnt = no_barrack(n, enemy, can_attack=n - b if b > 0 else 0,opt=True)
    if not flag:
        print(ans + cnt)