## N과 M (12)
## https://www.acmicpc.net/problem/15666


n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split())))) # 중복을 제거하고 정렬한다
n = len(nums) # 중복이 제거된 크기로 변경
temp = []

def func(k, dep):
    if dep == m: # 정해진 길이가 되면 출력하고 리턴
        print(" ".join(map(str, temp)))
        return
    
    for i in range(k,n):
        temp.append(nums[i])
        func(i, dep+1)
        temp.pop()
    
func(0, 0)