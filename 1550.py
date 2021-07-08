## 16진수
## https://www.acmicpc.net/problem/1550

# 파이썬의 내장함수를 이용하면 바로 16진수로 변경가능하지만 직접 구현함
# 0~9의 숫자면 입력된 값을 리턴하고 A~F면 10~15를 리턴한다
def hexToDec(n):
    if ord('0') <= ord(n) <= ord('9'):
        return int(n)
    return ord(n) - ord('A') + 10

n = list(input())
res = 0
cnt = 0
while n:
    # 리스트의 맨 뒤부터 자리수를 올려주며 10진수값 res에 더해준다
    res += hexToDec(n.pop()) * (16**cnt)
    cnt += 1

print(res)