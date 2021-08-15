## 방학숙제
## https://www.acmicpc.net/problem/5532

arr = [0, 0, 0, 0, 0]
days = [0, 0]
for i in range(5):
    arr[i] = int(input())

# 국어와 수학을 푸는데 필요한 날짜를 각각 계산한다
# 남은 페이지가 풀 수 있는 페이지보다 적어도 하루를 더 쓰므로 올림처리한다
for i in range(2):
    days[i] = arr[i+1] // arr[i+3]
    if arr[i+1] % arr[i+3] > 0:
        days[i] += 1
        
# 국어, 수학 둘 중 더 많이 소요되는 날짜를 뺀다
print(arr[0]-max(days))