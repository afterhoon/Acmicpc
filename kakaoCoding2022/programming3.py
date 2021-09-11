## fees: 기본시간 기본요금 단위시간 단위요금
## records: ["시:분 차량번호 내역(IN/OUT)"]

# 기본요금 + [(총시간-기본시간)/단위시간] * 단위시간 ([]는 올림)

import math

def solution(fees, records):
    answer = []

    basicTime = fees[0]
    basicFee = fees[1]
    unitTime = fees[2]
    unitFee = fees[3]
    car = [0 for i in range(10000)]
    park = [False for i in range(10000)]

    for i in range(len(records)):
        time, carNum, io = map(str, records[i].split())
        min = int(time[0:2]) * 60 + int(time[3:5])
        carNum = int(carNum)
        if io == "IN":
            car[carNum] -= min
            park[carNum] = True
        else:
            car[carNum] += min
            park[carNum] = False

    for i in range(10000):
        if park[i] == True:
            car[i] += 23 * 60 + 59
            park[i] = False

        if car[i] != 0:
            if basicTime >= car[i]:
                answer.append(basicFee)
            else:
                answer.append(basicFee + math.ceil((car[i]-basicTime)/unitTime) * unitFee)

    return answer