# HW 02. 트리플로 가

INF = -999999

def go_triple(num_of_vertex, vertex_list):
    my_point_list = [INF for _ in range(num_of_vertex+1)]
    
    for idx in range(num_of_vertex+1):
        if idx <= 0:
            my_point_list[0] = 0
        elif idx <= 1:
            my_point_list[idx] = my_point_list[idx-1] + vertex_list[idx]
        elif idx <= 2:
            my_point_list[idx] = max(my_point_list[idx-1] + vertex_list[idx] \
                                     , my_point_list[idx-2] + vertex_list[idx])
        else:
            if idx % 3 == 0:
                my_point_list[idx] = max(my_point_list[idx-1] + vertex_list[idx] \
                                         , my_point_list[idx-2] + vertex_list[idx] \
                                         , my_point_list[idx//3] + vertex_list[idx])
            else:
                my_point_list[idx] = max(my_point_list[idx-1] + vertex_list[idx] \
                                         , my_point_list[idx-2] + vertex_list[idx])            
    print(my_point_list[-1])

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_of_vertex = int(input())
        vertex_list = list(map(int, input().split()))
        vertex_list.insert(0, 0)
        go_triple(num_of_vertex, vertex_list)

if __name__ == "__main__":
    main()