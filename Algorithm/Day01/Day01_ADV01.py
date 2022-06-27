# ADV 01. 마을회관 건설
num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    house_list = list(map(int, input().split()))
    head_idx = 0
    tail_idx = max(house_list)
    while head_idx < tail_idx:
        middle_idx = tail_idx - (tail_idx - head_idx) // 2
        middle_l1 = sum(list(map(lambda x : abs(x-middle_idx), house_list)))
        head_l1 = sum(list(map(lambda x : abs(x-head_idx), house_list)))
        tail_l1 = sum(list(map(lambda x : abs(x-tail_idx), house_list)))
        if middle_l1 > head_l1:
            tail_idx = middle_idx - 1
        elif middle_l1 > tail_l1:
            head_idx = middle_idx + 1
        else:
            tail_idx = tail_idx - (tail_idx - middle_idx) // 2
            head_idx = middle_idx - (middle_idx - head_idx) // 2
    
    last_check_l1 = head_l1 if head_l1 < tail_l1 else tail_l1
    middle_l1 = middle_l1 if middle_l1 < last_check_l1 else last_check_l1

    print(middle_l1)