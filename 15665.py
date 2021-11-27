## N과 M (11)
## https://www.acmicpc.net/problem/15665


def func(k):
    if k > m: #정해진 수열의 길이가 되면 recursive 종료
        print(" ".join(map(str, temp)))
        return
    for i in range(n):
        temp.append(arr[i])
        func(k+1) #정해진 수열의 길이가 될때까지 반복
        temp.pop()

n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split())))) #set으로 중복제거한 리스트생성
n = len(arr)
temp = []

func(1)

