# 07. 우선순위 큐 구현하기

import heapq

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    num_of_query = int(input())
    temp_heap = list()
    for _ in range(num_of_query):
        command = int(input())
        if command == -1:
            print(heapq.heappop(temp_heap))
        else:
            heapq.heappush(temp_heap, command)