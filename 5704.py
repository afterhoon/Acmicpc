## 팬그램
## https://www.acmicpc.net/problem/5704

while True:
    s = list(input().replace(" ", "")) # 공백을 제거하고 문자열을 리스트로 받는다
    if s[0] == "*": # '*' 이 입력되면 프로그램 종료
        break

    s = list(set(s)) # 중복되는 문자들을 제거
    
    # 중복된 문자들을 모두 제거했을 때 리스트의 크기가 알파벳의 개수인 26이라면 팬그램이다
    print("Y" if len(s) == 26 else "N") 