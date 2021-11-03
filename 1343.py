## 폴리오미노
## https://www.acmicpc.net/problem/1343

s = input()

# 받은 문자열에서 "XXXX"를 "AAAA"로 모두 치환한 뒤
# 그 문자열에서 다시 "XX"를 "BB"로 치환한다
s = s.replace("XXXX", "AAAA").replace("XX", "BB")
print("-1" if 'X' in s else s) # 치환된 문자열에 X가 남아있으면 -1 출력
