## 검증수
## https://www.acmicpc.net/problem/2475

n = list(map(int, input().split()))
sum = 0
# 입력받은 각 숫자를 pow() 함수로 제곱수로 만들고 sum에 더해준다
for i in range(len(n)):
    sum += pow(n[i], 2)
# sum을 10으로 나눈 나머지 출력
print(sum%10)