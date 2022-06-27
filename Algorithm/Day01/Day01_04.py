num_of_list = int(input())
for _ in range(num_of_list):
    temp_list = list(map(int, input().split()))
    print(max(temp_list) - min(temp_list))