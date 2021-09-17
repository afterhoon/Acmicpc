## N과 M (4)
## https://www.acmicpc.net/problem/15652

arr = []

def func(begin, n, m):
    # 최초에 m개의 숫자를 고른다고 할때 한개를 고를때마다 m-1을 해주고
    # m이 0이 되면 모든 숫자를 고른것이므로 선택된 숫자 리스트를 출력한다
    if m == 0:
        print(" ".join(map(str, arr)))
        return
    # 시작숫자(앞숫자와 같거나 큰 숫자) 부터 순서대로 리스트에 넣는다
    for i in range(begin, n):
        arr.append(i+1)
        func(i, n, m-1)
        arr.pop()

n, m = map(int, input().split())
func(0, n, m)
