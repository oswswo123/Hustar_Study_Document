# Day 02 - PJ 02. 이진 탐색 2

def binary_search(test_list, search_value):
    head_idx = 0
    tail_idx = len(test_list) - 1
       
    while head_idx < tail_idx-1:
        middle_idx = head_idx + (tail_idx - head_idx) // 2
        if search_value <= test_list[middle_idx]:
            tail_idx = middle_idx
        else:
            # search_value > test_list[middle_idx]:
            head_idx = middle_idx
    
    if search_value == test_list[tail_idx]:
        return test_list[tail_idx]
    elif search_value == test_list[head_idx]:
        return test_list[head_idx]
    else:
        return test_list[head_idx] if abs(search_value - test_list[head_idx]) <= abs(search_value - test_list[tail_idx]) else test_list[tail_idx]
            

num_of_testcase = int(input())
for _ in range(num_of_testcase):
    test_list = list(map(int, input().split()))
    search_value_list = list(map(int, input().split()))
    output_list = list()
    for search_value in search_value_list:
        output_list.append(binary_search(test_list, search_value))
    
    print(*output_list)    
    