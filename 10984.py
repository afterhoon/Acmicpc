## 내 학점을 구해줘
## https://www.acmicpc.net/problem/10984

t = int(input())
for _ in range(t):
    n = int(input())
    credit = 0
    gpa = 0
    for i in range(n):
        c, g = map(float, input().split())
        c = int(c)
        credit += c # 학점의 합계를 구함
        gpa += c * g # 점수 평균을 구하기 위해 총합을 입력
    gpa /= credit # 학점 1점당으로 나눠준다
    gpa = round(gpa, 1) # 소수점 첫째자리까지 반올림
    print(credit, gpa)