## 돌 게임2
## https://www.acmicpc.net/problem/9656

n = int(input())
print("CY" if n%2 else "SK")

'''
돌의 개수에 따라 이기는 경우는 다음과 같다

개수    1   2   3   4   5   6   7
상근    1       1       1
찬영        1       1       1

따라서 홀수번에는 상근, 짝수번은 찬영으로 출력해준다
'''