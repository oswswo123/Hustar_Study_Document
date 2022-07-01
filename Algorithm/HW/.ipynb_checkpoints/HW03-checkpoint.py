# HW 03. 이진 탐색 6

import bisect

def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list[len(unsorted_list)//2]
        lower_list, equal_list, upper_list = list(), list(), list()
        
        for element in unsorted_list:
            if element > pivot:
                upper_list.append(element)
            elif element < pivot:
                lower_list.append(element)
            else:
                equal_list.append(element)
            
        return quick_sort(lower_list) + equal_list + quick_sort(upper_list)

def count_upper_number(sorted_list, search_value):
    right_idx = bisect.bisect_right(sorted_list, search_value)
    return right_idx

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        unsorted_list = list(map(int, input().split()))
        check_number = list(map(int, input().split()))
        output_list = list()
        
        sorted_list = quick_sort(unsorted_list)
        for search_value in check_number:
            upper_idx = count_upper_number(sorted_list, search_value)
            output_list.append(len(sorted_list) - upper_idx)
        
        print(*output_list)

if __name__ == "__main__":
    main()