def solution(id_list, report, k):
    id_size = len(id_list)   

    answer = [0 for i in range(id_size)]
    reported = [[] for i in range(id_size)]

    for i in range(len(report)):
        m,n = map(str, report[i].split())
        if m not in reported[id_list.index(n)]:
            reported[id_list.index(n)].append(m)

    for i in range(id_size):
        temp_size = len(reported[i])
        if temp_size >= k:
            for j in range(temp_size):
                answer[id_list.index(reported[i][j])] += 1
    
    return answer