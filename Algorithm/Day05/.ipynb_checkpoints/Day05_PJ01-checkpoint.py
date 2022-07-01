# Day 05 - PJ. 01 최대 합 부분 연속 수열 2

INF = -999999

def max_sum_subsequence_dp(test_sequence):
    max_sum_sub_dp = [INF for _ in test_sequence]
    for idx, value in enumerate(test_sequence):
        if idx == 0:
            max_sum_sub_dp[idx] = value
        else:
            max_sum_sub_dp[idx] = max(max_sum_sub_dp[idx-1]+value, value)
    
    return max(max_sum_sub_dp)

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        test_sequence = list(map(int, input().split()))
        print(max_sum_subsequence_dp(test_sequence))

if __name__ == "__main__":
    main()