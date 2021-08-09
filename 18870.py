## 좌표 압축
## https://www.acmicpc.net/problem/18870

n = int(input())
x = list(map(int, input().split()))

# x에서 중복을 없애주고 정렬해준다
sorted_x = sorted(list(set(x)))
# 각 숫자를 크기순으로 대응시켜 딕셔너리에 입력해준다
dic = {sorted_x[i] : i for i in range(len(sorted_x))}
# 각 딕셔너리의 인덱스로 입력하여 대응되는 순서가 출력한다
for i in x:
    print(dic[i], end = ' ')