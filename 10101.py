## 삼각형 외우기
## https://www.acmicpc.net/problem/10101

angle = []
ans = ""
for _ in range(3):
    angle.append(int(input()))

if sum(angle) == 180:
    if angle[0] == angle[1] == angle[2]:
        ans = "Equilateral" 
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]:
        ans = "Isosceles"
    else:
        ans = "Scalene"
else:
    ans = "Error"

print(ans)