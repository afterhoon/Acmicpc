def solution(n, info):
    answer = [0 for i in range(11)]
    stuff = [[0,0]]

    knapsack = [[0 for _ in range(n + 1)] for _ in range(10 + 1)]

    for i in range(10):
        temp = (10-i)/(info[i]+1)
        if info[i] > 0:
            temp *= 2
        stuff.append([info[i]+1, temp])

    for i in range(1, 10 + 1):
        for j in range(1, n + 1):
            arrow = stuff[i][0] 
            value = stuff[i][1]
        
            if j < arrow:
                knapsack[i][j] = knapsack[i - 1][j]
            else:
                a = value + knapsack[i - 1][j - arrow]
                b = knapsack[i - 1][j]
                if a > b:
                    knapsack[i][j] = a
                    answer[i] = 1
                else:
                    knapsack[i][j] = b

    answer = answer[1:11]
    return answer

print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))