# ADV 02. 가장 가까운 두 점

def calculate_l1dist(first_dot, second_dot):
    return abs(first_dot[0] - second_dot[0]) + abs(first_dot[1] - second_dot[1])

def find_min_l1dist(dot_list, head_idx, tail_idx):
    if head_idx == tail_idx:
        return 999999
    
    if tail_idx - head_idx == 1:
        return calculate_l1dist(dot_list[head_idx], dot_list[tail_idx])
    
    middle_idx = (head_idx + tail_idx) // 2
    temp_min_l1dist = min(find_min_l1dist(dot_list, head_idx, middle_idx), find_min_l1dist(dot_list, middle_idx, tail_idx))
    
    middle_dot = list()
    for idx in range(head_idx, tail_idx):
        if abs(dot_list[idx][0] - dot_list[middle_idx][0]) < temp_min_l1dist:
            middle_dot.append(dot_list[idx])
    
    middle_dot = sorted(middle_dot, key=lambda x:x[1])
    for first_idx in range(len(middle_dot)-1):
        for second_idx in range(first_idx+1, len(middle_dot)):
            if abs(middle_dot[first_idx][1] - middle_dot[second_idx][1]) < temp_min_l1dist:
                temp_min_l1dist = min(calculate_l1dist(middle_dot[first_idx], middle_dot[second_idx]), temp_min_l1dist)
            else:
                break
    
    return temp_min_l1dist

num_of_testcase = int(input())
for _ in range(num_of_testcase):
    num_of_dot = int(input())
    dot_list = list()
    
    for _ in range(num_of_dot):
        dot_list.append(tuple(map(int, input().split())))
    
    dot_list = sorted(dot_list, key=lambda x:x[0])
    min_l1dist = find_min_l1dist(dot_list, 0, len(dot_list)-1)
    
    print(min_l1dist)