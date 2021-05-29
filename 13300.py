## 방 배정
## https://www.acmicpc.net/problem/13300

K, N = map(int, input().split())
std = [0 for i in range(12)]
sum = 0

## 각 학년 및 성별로 구분되는 크기 12의 리스트(std)에 학생수 입력
## std[0]: 1학년여자 / std[1]: 1학년남자 / std[2]: 2학년여자 / std[3]: 2학년남자 ...
## std[(학년-1)*2 + 성별코드]
for i in range(K):
    S, Y = map(int, input().split())
    std[(Y-1)*2 + S] += 1

## 각 학생들의 수를 가져와서 방의 최대크기(N)로 나누어줘서 필요한 총 방의 개수(sum)에 더해주고
## 나누어주는 과정에서 남는 학생이 있으면 추가로 방배정을 해줘야하므로 1 추가
for i in range(12):
    sum += std[i] // N
    if std[i]%N > 0:
        sum += 1

print(sum)