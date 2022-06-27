# PJ 01. 두 바퀴 레이스
import collections

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    race_data = input().split()
    test_queue = collections.deque(list())
    for element in race_data:
        if element in test_queue:
            if element == test_queue[0]:
                test_queue.popleft()
            else:
                break
        else:
            test_queue.append(element)
    
    if bool(test_queue) == False:
        print("NO")
    else:
        print("YES")