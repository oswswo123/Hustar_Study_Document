# Day 02 - PJ 01. 합병 (merge)

def merge(first_test_list, second_test_list):
    temp_list = list()
    
    first_list_head = 0
    first_list_tail = len(first_test_list)
    
    second_list_head = 0
    second_list_tail = len(second_test_list)

    while first_list_head < first_list_tail and second_list_head < second_list_tail:
        if first_test_list[first_list_head] < second_test_list[second_list_head]:
            # temp_list.append(first_test_list[first_list_head])
            temp_list.append("1")
            first_list_head += 1
        elif first_test_list[first_list_head] > second_test_list[second_list_head]:
            # temp_list.append(second_test_list[second_list_head])
            temp_list.append("2")
            second_list_head += 1
        else:
            # 조건상 일어나지 않음
            pass
    
    if first_list_head >= first_list_tail:
        for idx in range(second_list_head, second_list_tail):
            # temp_list.append(second_test_list[idx])
            temp_list.append("2")
    else:
        for idx in range(first_list_head, first_list_tail):
            # temp_list.append(first_test_list[idx])
            temp_list.append("1")
    
    return temp_list

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    first_test_list = list(map(int, input().split()))
    second_test_list = list(map(int, input().split()))
    print(*merge(first_test_list, second_test_list))