## N과 M (8)
## https://www.acmicpc.net/problem/15657

# 반복을 할때 시작인덱스와 몇번째 숫자인지를 나타내는 depth를 매개변수로 가진다
def func(start, depth):
    # depth가 m과 같으면 모두 입력됐으므로 출력하고 반복을 종료한다
    if depth == m:
        print(" ".join(map(str, temp)))
        return

    # start부터 인덱스 끝까지 temp에 입력하며 재귀한다
    for i in range(start, n):
        temp.append(arr[i])
        func(i, depth+1)
        temp.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = []

func(0, 0)