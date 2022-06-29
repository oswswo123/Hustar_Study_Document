## ADV 02. 가장 가파른 두 점

def create_adjacent_list(test_list):
    adjacent_list = list()
    test_list = sorted(test_list, key=lambda x:x[0])
    
    for idx_first in range(0, len(test_list)-1):
        adjacent_list.append([test_list[idx_first], test_list[idx_first+1]])
    
    return adjacent_list

def calculate_gradient(set_of_adjacent_dot):
    gradient_list = list()
    
    for dot_set_element in set_of_adjacent_dot:
        gradient = abs((dot_set_element[0][1] - dot_set_element[1][1]) / (dot_set_element[0][0] - dot_set_element[1][0]))
        gradient_list.append([gradient, dot_set_element[0], dot_set_element[1]])
        
    return gradient_list

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    num_of_count = int(input())
    test_list = list()
    
    for _ in range(num_of_count):
        test_list.append(list(map(int, input().split())))
    
    set_of_adjacent_dot = create_adjacent_list(test_list)
    set_of_gradient = calculate_gradient(set_of_adjacent_dot)
    max_gradient_set = max(set_of_gradient, key=lambda x:x[0])
    output_str = " ".join(list(map(str, max_gradient_set[1]))) + " " + " ".join(list(map(str, max_gradient_set[2])))
    
    print(output_str)