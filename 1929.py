## 소수 구하기
## https://www.acmicpc.net/problem/1929

import math
m, n = map(int, input().split())

def isPrime(m, n):
    # 각 숫자의 소수유무를 입력받을 prime 리스트 생성
    prime = [True] * n
    # 배수를 다 제외할것이기 때문에 제곱근까지만 반복한다
    for i in range(2, int(math.sqrt(n))+1):
        # 어떤 숫자가 소수라면 그 소수의 배수는 모두 소수가 아니므로 False로 변경해준다 (자기가 아닌 가장 작은 배수는 2*i 이므로 2*i부터 시작)
        if prime[i]:
            for j in range(2*i, n, i):
                prime[j] = False

    # prime리스트가 true인 것만 출력
    for i in range(m, n):
        if i > 1 and prime[i] == True:
            print(i)

isPrime(m, n+1)