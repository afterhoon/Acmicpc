## 뒤집힌 덧셈
## https://www.acmicpc.net/problem/1357

x, y = input().split()
# string 변수로 받아서 뒤집어준다
x = x[::-1]
y = y[::-1]
# 뒤집어진 두 수를 int형으로 바꿔 계산한 뒤 다시 string으로 변환해 ans에 입력해준다
ans = str(int(x)+int(y))

# ans를 뒤집은뒤 int형으로 변환해준다
# (형변환 안해줄시 1 + 9 같은 경우에 앞에 0이 출력되므로 실패)
print(int(ans[::-1]))