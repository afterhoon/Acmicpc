## 10부제
## https://www.acmicpc.net/problem/10797

n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    # 리스트를 확인해서 차번이 날짜와 같다면 cnt를 1 추가한다
    if (num == n):
        cnt += 1

print(cnt)