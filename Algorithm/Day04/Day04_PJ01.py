# Day 04 - PJ 01. 부산에서 서울로

def check_can_go(oil_capacity, gas_station_list):
    now_position = 0
    visited_list = [0]
    
    while now_position < len(gas_station_list)-1:
        check_position = now_position + 1
        if gas_station_list[check_position] - gas_station_list[now_position] > oil_capacity:
            break
        else:
            while check_position < len(gas_station_list)-1:
                if gas_station_list[check_position+1] - gas_station_list[now_position] <= oil_capacity:
                    check_position += 1
                else:
                    break
            now_position = check_position
            visited_list.append(gas_station_list[now_position])

    if visited_list[-1] == gas_station_list[-1]:
        return len(visited_list[1:-1])
    else:
        return -1

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        oil_capacity, b_to_s_distance = tuple(map(int, input().split()))
        gas_station_list = list(map(int, input().split()))
        gas_station_list.insert(0, 0)
        gas_station_list.append(b_to_s_distance)
        print(check_can_go(oil_capacity, gas_station_list))
        

if __name__ == "__main__":
    main()