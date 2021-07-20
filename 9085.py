## 더하기
## https://www.acmicpc.net/problem/9085

T = int(input())
for t in range(T):
    n  = int(input())
    # 리스트에 입력받은후 sum() 함수로 합을 출력
    arr = list(map(int, input().split()))
    print(sum(arr))