# 02. 이진 탐색 1

def binary_search(test_list, search_value):
    head_idx = 0
    tail_idx = len(test_list) - 1
    while head_idx <= tail_idx:
        middle_idx = tail_idx - (tail_idx - head_idx) // 2
        if search_value < test_list[middle_idx]:
            tail_idx = middle_idx - 1
        elif search_value > test_list[middle_idx]:
            head_idx = middle_idx + 1
        else:
            break

    if search_value == test_list[middle_idx]:
        return middle_idx
    else:
        return -1

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    test_list = list(map(int, input().split()))
    search_value_list = list(map(int, input().split()))
    output_list = list()
    
    for search_value in search_value_list:
        output_list.append(binary_search(test_list, search_value))
    
    print(*output_list)