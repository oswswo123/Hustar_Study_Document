## ADV 02. 가장 가파른 두 점

def create_combination(test_list):
    set_of_dot = list()
    for idx_first, dot_item_first in enumerate(test_list[0:-1]):
        for idx_second, dot_item_second in enumerate(test_list[idx_first+1:]):
            set_of_dot.append([dot_item_first, dot_item_second])
    
    return set_of_dot

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    num_of_count = int(input())
    test_list = list()
    for _ in range(num_of_count):
        test_list.append(list(map(int, input().split())))
    
    set_of_dot = create_combination(test_list)
    gradient_list = list(map(lambda x : abs((x[0][1]-x[1][1]) / (x[0][0]-x[1][0])), set_of_dot))
    max_gradient_idx = gradient_list.index(max(gradient_list))
    last_output = sorted(set_of_dot[max_gradient_idx], key=lambda x : x[0])
    output_str = " ".join(list(map(str, last_output[0]))) + " " + " ".join(list(map(str, last_output[1])))
    print(output_str)