## N번째 큰 수 
## https://www.acmicpc.net/problem/2693

# T = case 개수
T = int(input());

for _ in range(T):
    # num이라는 list에 10개의 수 입력
    num = list(map(int, input().split()));
    # sort() 함수로 오름차순 정렬
    num.sort();
    # 세번째로 큰 수 = -3 = 7
    print(num[-3]);