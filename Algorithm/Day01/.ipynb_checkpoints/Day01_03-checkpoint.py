num_of_list = int(input())
for _ in range(num_of_list):
    temp_list = input().split()
    temp_list = [int(item) for item in temp_list]
    print(sum(temp_list))