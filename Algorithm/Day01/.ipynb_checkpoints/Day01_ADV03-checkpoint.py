# ADV 03. N 바퀴 레이스
import collections

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    num_of_lab = int(input())
    race_data = input().split()
    test_queue = [collections.deque(list()) for _ in range(num_of_lab)]
    car_lab_hash = dict()
    for element in race_data:
        if element not in car_lab_hash:
            car_lab_hash[element] = 0
            if element in test_queue[0]:
                if element == test_queue[0][0]:
                    test_queue[0].popleft()
                else:
                    break
            else:
                test_queue[0].append(element)
        else:
            if element == test_queue[car_lab_hash[element]][0]:
                test_queue[car_lab_hash[element]+1].append(test_queue[car_lab_hash[element]].popleft())
                car_lab_hash[element] += 1
            else:
                break
                
    is_change = list()
    for queue_element in test_queue[:-1]:
        is_change.append(False if bool(queue_element) else True)

    if all(is_change):
        print("NO")
    else:
        print("YES")