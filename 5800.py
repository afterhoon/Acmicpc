## 성적 통계
## https://www.acmicpc.net/problem/5800

k = int(input())
for i in range(k):
    s = list(map(int, input().split()))

    # 리스트에서 학생수를 빼주고 정렬
    l = s[0]
    del s[0]
    s.sort()

    # 최대 차이를 저장
    diff = 0
    for j in range(l-1):
        diff = max(diff, s[j+1]-s[j])

    print("Class", i+1)
    print("Max ", s[l-1], ", Min ", s[0], ", Largest gap ", diff, sep="")