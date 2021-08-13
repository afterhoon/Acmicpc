## 오각형,오각형,오각형
## https://www.acmicpc.net/problem/1964

n = int(input())
ans = 5 # 첫 점의 개수
inc = 7 # 최초로 증가하는 점의 개수 (이후 3씩 증가)

# increment는 매번 3씩 증가한다
# (첫번째에는 반복문에 들어오지 않고 5로 출력된다)
for i in range(1, n):
    ans += inc
    inc += 3
print(ans % 45678)
