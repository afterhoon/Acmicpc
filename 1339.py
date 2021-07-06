## 단어 수학
## https://www.acmicpc.net/problem/1339

n = int(input())
# 알파벳 A~Z의 크기를 입력해둘 alp 리스트를 선언한다
# 단 alp 리스트의 뒷 두자리는 알파벳의 순서를 따로 입력해두고 건드리지 않는다
alp = [i for i in range(26)]
ans = 0
for i in range(n):
    temp = list(input())
    cnt = 2 # 맨 뒷 두자리는 알파벳의 순서기 때문에 10^2 부터 입력
    # 입력받은 문자열의 각 알파벳을 대응되는 alp리스트의 인덱스에 크기를 입력한다
    while(temp):
        idx = ord(temp.pop()) - ord('A')
        alp[idx] += 1 * 10**cnt
        cnt += 1

# alp 리스트를 정렬한다 (오름차순이므로 맨 뒤가 가장 큼)
alp.sort()
num = 9
# alp 리스트의 가장 큰 수부터 맨 뒤 두자리를 제외한 뒤
# 9부터 순서대로 합쳐서 답에 더해간다
while True:
    val = alp.pop() // 100
    if val <= 0:
        break
    ans += val * num
    num -= 1

print(ans)