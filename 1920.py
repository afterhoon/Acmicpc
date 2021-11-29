## 수 찾기
## https://www.acmicpc.net/problem/1920

def func(target, start, end, data): #이분탐색 알고리즘을 구현한다
    if start > end: #start가 end보다 커지는 것은 리스트 내에 target이 없다는것을 의미한다
        return 0
    
    mid = (start + end) // 2

    if data[mid] == target: #값을 찾았으므로 1을 리턴한다
        return 1
    elif data[mid] > target: #중간값이 target보다 크다면 target은 앞지점과 중간값 사이에 있다고 할수 있다
        end = mid - 1
    else: #중간값이 target보다 크다면 target은 중간값과 뒷지점 사이에 있다고 할수 있다
        start = mid + 1
    
    return func(target, start, end, data) #변경된 start와 end를 통해 함수를 재귀 호출한다

n = int(input())
a = sorted(list(map(int, input().split()))) #이분탐색을 진행하기 전에 리스트를 정렬한다
m = int(input())
x = list(map(int, input().split()))

for i in range(m):
    print(func(x[i], 0, n-1, a))