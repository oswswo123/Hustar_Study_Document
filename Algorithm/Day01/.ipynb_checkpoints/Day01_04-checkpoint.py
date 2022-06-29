# 04. 최댓값과 최솟값의 차
num_of_list = int(input())
for _ in range(num_of_list):
    temp_list = list(map(int, input().split()))
    print(max(temp_list) - min(temp_list))