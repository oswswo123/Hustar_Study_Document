# 03. 암기대회

def create_dp_point_map(point_map, row_size, col_size):
    dp_point_map = list()
    for _ in range(row_size):
        dp_point_map.append([0 for _ in range(col_size)])
        
    for row_idx in range(row_size):
        for col_idx in range(col_size):
            if row_idx == 0:
                if col_idx == 0:
                    dp_point_map[row_idx][col_idx] = point_map[row_idx][col_idx]
                else:
                    dp_point_map[row_idx][col_idx] = point_map[row_idx][col_idx] + dp_point_map[row_idx][col_idx-1]
            elif col_idx == 0:
                dp_point_map[row_idx][col_idx] = point_map[row_idx][col_idx] + dp_point_map[row_idx-1][col_idx]
            else:
                dp_point_map[row_idx][col_idx] = min(point_map[row_idx][col_idx] + dp_point_map[row_idx-1][col_idx] \
                                                    , point_map[row_idx][col_idx] + dp_point_map[row_idx][col_idx-1] \
                                                    , point_map[row_idx][col_idx] + dp_point_map[row_idx-1][col_idx-1])
    return dp_point_map[-1][-1]

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        row_size, col_size = tuple(map(int, input().split()))
        point_map = list()
        
        for _ in range(row_size):
            point_map.append(list(map(int, input().split())))
            
        print(create_dp_point_map(point_map, row_size, col_size))

if __name__ == "__main__":
    main()