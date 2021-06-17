## 암호 만들기
## https://www.acmicpc.net/problem/1759

from itertools import combinations

l, c = map(int, input().split())
# 결과값이 정렬된 상태여야하기 때문에 입력받은 값을 미리 정렬해준다
alp = sorted(list(map(str, input().split())))

# 각 숫자는 한번씩만 출력되어야 하므로 조합(combination)을 이용한다
temp = combinations(alp, l)
mo_enum = ['a', 'e', 'i', 'o', 'u']

for pw in temp:
    # 자음개수(ja)와 모음개수(mo)를 확인할 변수를 0으로 초기화하고 자음이 2개이상 모음이1개 이상일 경우에만 출력한다
    ja = 0
    mo = 0
    for el in pw:
        if el in mo_enum:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        print(''.join(pw))
