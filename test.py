import math 
import time 
import heapq
start = time.time() 

heap = []

oper_num = int(input())
for _ in range(oper_num):
    input_num = int(input())
    if input_num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, input_num)


end = time.time() 
print(f"{end - start:.5f} sec")

'''
import math 
import time 
import heapq
start = time.time() 

heap = []
arr = []
oper_num = int(input())
for _ in range(oper_num):
    input_num = int(input())
    if input_num == 0:
        if heap:
            arr.append(heapq.heappop(heap))
        else:
            arr.append(0)
    else:
        heapq.heappush(heap, input_num)

for el in arr:
    print(el)

end = time.time() 
print(f"{end - start:.5f} sec")

'''