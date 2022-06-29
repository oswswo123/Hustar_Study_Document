# ADV 01. 이진 탐색 3

import bisect

def quick_sort(test_list):
    if len(test_list) <= 1:
        return test_list
    else:
        pivot = test_list[len(test_list) // 2]
        lower_list, equal_list, upper_list = list(), list(), list()
        
        for num_element in test_list:
            if num_element < pivot:
                lower_list.append(num_element)
            elif num_element > pivot:
                upper_list.append(num_element)
            else:
                equal_list.append(num_element)
        
        return quick_sort(lower_list) + equal_list + quick_sort(upper_list)

def bisect_find(sorted_first_list, search_value):
    left_idx = bisect.bisect_left(sorted_first_list, search_value)
    right_idx = bisect.bisect_right(sorted_first_list, search_value)
    
    return right_idx - left_idx

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    first_list = list(map(int, input().split()))
    second_list = list(map(int, input().split()))
    
    sorted_first_list = quick_sort(first_list)
    output = 0
    for search_value in second_list:
        output += bisect_find(sorted_first_list, search_value)
    
    print(output)