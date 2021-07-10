## '나교수' 교수님의 악필
## https://www.acmicpc.net/problem/16462

# 기본적인 round() 함수를 쓰면 사사오입 원칙에 따라 짝수로 쏠리는 경향이 있다
# 따라서 일반적인 반올림을 위해 직접 구현하였다
def myRound(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    return int(n)

n = int(input())
q = []

for i in range(n):
    score = input()
    mod_score = ""

    # 100일 경우 바로 100으로 리스트에 입력해준다
    if score == "100":
        mod_score = "100"
    # 이외의 숫자는 0,6,9 중 해당하는지 확인 후 해당하면 9로 변경하여 입력해준다
    else:
        for c in score:
            if c in ['0', '6', '9']:
                c = '9'
            mod_score += c
    q.append(int(mod_score))

# 평균값을 myRound() 함수를 이용해 반올림해서 출력한다
print(myRound(sum(q)/len(q)))