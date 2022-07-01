# 02. 배송비 절약

def find_min_delivery_fee(num_of_thing, weight_limit, thing_list):
    min_cost_dp = list()
    for _ in range(num_of_thing):
        min_cost_dp.append([0 for _ in range(weight_limit+1)])
        
    for kind_of_thing in range(num_of_thing):
        for now_weight in range(1, weight_limit+1):
            if kind_of_thing == 0:
                if now_weight >= thing_list[kind_of_thing][0]:
                    min_cost_dp[kind_of_thing][now_weight] = thing_list[kind_of_thing][1]
                else:
                    min_cost_dp[kind_of_thing][now_weight] = 0
            else:
                if now_weight >= thing_list[kind_of_thing][0]:
                    remove_before_thing_idx = now_weight-thing_list[kind_of_thing][0] if now_weight-thing_list[kind_of_thing][0] >= 0 else 0
                    min_cost_dp[kind_of_thing][now_weight] = max(min_cost_dp[kind_of_thing-1][now_weight], \
                                                                min_cost_dp[kind_of_thing-1][remove_before_thing_idx] + thing_list[kind_of_thing][1])
                else:
                    min_cost_dp[kind_of_thing][now_weight] = min_cost_dp[kind_of_thing-1][now_weight]

    return min_cost_dp[-1][-1]

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_of_thing, weight_limit = tuple(map(int, input().split()))
        weight_list = tuple(map(int, input().split()))
        value_list = tuple(map(int, input().split()))
        thing_list = [thing_data for thing_data in zip(weight_list, value_list)]
        print(find_min_delivery_fee(num_of_thing, weight_limit, thing_list))
        

if __name__ == "__main__":
    main()