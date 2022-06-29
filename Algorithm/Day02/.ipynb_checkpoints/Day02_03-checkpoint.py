# 03. 최대 합 부분 연속 수열

def find_maxsum_sublist(test_list):
    if len(test_list) <= 1:
        return test_list[0]
    else:
        tail_idx = len(test_list)
        middle_idx = tail_idx // 2
        
        left_maxsum = find_maxsum_sublist(test_list[0:middle_idx])
        right_maxsum = find_maxsum_sublist(test_list[middle_idx:tail_idx])
        
        lmax = -99999
        lsum = 0
        for idx in range(middle_idx-1, -1, -1):
            # lmax 구하기
            lsum += test_list[idx]
            if lmax < lsum:
                lmax = lsum
        
        rmax = -99999
        rsum = 0
        for idx in range(middle_idx, tail_idx):
            # rmax 구하기
            rsum += test_list[idx]
            if rmax < rsum:
                rmax = rsum
        
        middle_maxsum = lmax + rmax
        
        return max([left_maxsum, right_maxsum, middle_maxsum])    

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    test_list = list(map(int, input().split()))
    print(find_maxsum_sublist(test_list))
    