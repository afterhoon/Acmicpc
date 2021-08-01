## 리모컨
## https://www.acmicpc.net/problem/1107

n = int(input())
m = int(input())
broken = []
# m이 0일 경우 입력을 받지 않는다 (해당 부분 제외시 EOF 런타임 에러)
if m > 0:
    broken = list(map(int, input().split()))
# 고장난 숫자키 broken을 제외한 수들을 입력한다
num = [str(i) for i in range(10) if i not in broken]
# 최초에 숫자키를 입력하지않고 +/- 버튼만 이용했을때의 수를 센다
cnt = abs(n - 100)

# 찾는 채널은 500000까지지만 버튼이 9빼고 고장났을경우 
# 999999밖에 입력하지 못하므로 0 <= i < 1000000 까지 반복한다
# (50만까지로 하면 예제 3번째 case에서 실패)
'''
# 예제3 (range(500000)의 경우)
   입력                 출력                정답                
   500000               344451              11117
   8
   0 2 3 4 6 7 8 9
'''
for i in range(1000000):
    channel = str(i)
    # 채널의 각 자릿수마다 누를수 있는 숫자키인지 판단하고 아니라면 다음 채널로 넘어간다
    # 누를수 있는 채널이라면 기존에 입력된 값과 비교해 더 작은 수를 채택한다
    for j in range(len(channel)):
        if channel[j] not in num:
            break
        if j == len(channel) - 1:
            cnt = min(cnt, abs(i-n) + len(channel))

print(cnt)