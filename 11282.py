## 한글
## https://www.acmicpc.net/problem/11282

# '가'의 아스키코드 번호는 44032이고 한글은 여기부터 시작된다
# ord('가') 로 쉽게 알수 있다
n = int(input())
print(chr(44031+n))