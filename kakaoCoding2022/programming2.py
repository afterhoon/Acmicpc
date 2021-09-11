'''
제한사항
1 ≤ n ≤ 1,000,000
3 ≤ k ≤ 10
입출력 예
n	k	result
437674	3	3
110011	10	2
'''

NOTA = '0123456789ABCDEF'

def numeral(n, b):
    q, r = divmod(n, b)
    num = NOTA[r]
    return numeral(q, b) + num if q else num

pn = 1000000
a = [False,False] + [True]*(pn-1)
primes=[]

for i in range(2,pn):
    if a[i]:
        primes.append(i)
        for j in range(2*i, pn+1, i):
            a[j] = False

def solution(n, k):
    answer = 0
    transf = str(numeral(n, k)) + "0"
    print(transf)
    temp = 0
    for i in range(len(transf)):
        if transf[i] != '0':
            temp = temp * 10 + int(transf[i])
        else:
            if temp in primes:
                answer += 1
            temp = 0

    return answer

print(solution(1000000, 3))