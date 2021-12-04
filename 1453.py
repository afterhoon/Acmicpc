## 피시방 알바
## https://www.acmicpc.net/problem/1453

n = int(input())
guest = list(map(int, input().split()))
#중복된 손님은 거절되므로 중복을 제외하는 set으로 변경한 뒤 크기를 비교하면 된다
print(len(guest) - len(set(guest)))