## 문자가 몇갤까
## https://www.acmicpc.net/problem/7600

# 문자열에서 알파벳인지 비교할 알파벳 리스트 생성
alp = [chr(ord('a')+i) for i in range(26)]

while True:
    cnt = 0
    temp = input()
    if temp == "#":
        break

    # 입력받은 temp를 모두 소문자로 바꾸고 set()로 바꿔서 중복을 모두 제거한다
    temp = set(map(str, temp.lower()))

    # temp의 원소중에 알파벳을 발견하면 cnt를 1씩 증가시킨다
    for el in temp:
        if el in alp:
            cnt += 1
    print(cnt)
