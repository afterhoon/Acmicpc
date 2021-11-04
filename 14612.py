## 김식당
## https://www.acmicpc.net/problem/14612

n, m = map(int, input().split())
orders = []
for _ in range(n):
    s = list(input().split())

    if s[0] == "order": #(테이블번호, 주문시간)
        orders.append((int(s[1]), int(s[2])))
    
    elif s[0] == "sort": #주문시간순으로 정렬 (테이블번호가 같으면 번호가 작은것부터)
        orders.sort(key=lambda x : (x[1], x[0]))
    
    elif s[0] == "complete":
        for i in range(len(orders)):
            k, t = orders[i] #orders를 k(테이블번호), t(주문시간) 로 분리
            if k == int(s[1]):
                del orders[i] #요리가 완성된 테이블의 번호 제거
                break
    
    if len(orders) != 0: #포스트잇이 있다면 테이블 번호들 출력
        ans = ""
        for i in range(len(orders)):
            k, t = orders[i]
            ans += str(k) + " "
        print(ans[:len(ans)-1])
    else:
        print("sleep")
