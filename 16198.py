## 에너지 모으기
## https://www.acmicpc.net/problem/16198

n = int(input())
w = list(map(int, input().split()))
maxEng = 0

def energy(x, len):
    # 가장 큰 에너지를 maxEng에 저장한다
    global maxEng
    if len == 2:
        if x > maxEng:
            maxEng = x
    else:
        # 해당 원소 좌우를 곱해서 x에 더해주고
        # 그 원소가 제거된 배열로 재귀함수를 호출해준다
        # 모든 경우를 순회하면서 확인한다 
        # (이때 첫 호출은 온전한 배열에서 시작해야되므로 제거했던 원소를 다시 더해주고 시작한다)
        for i in range(1, len-1):
            eng = w[i-1] * w[i+1]
            temp = w[i]
            del w[i]
            energy(x + eng, len-1)
            w.insert(i, temp)

energy(0, n)
print(maxEng)