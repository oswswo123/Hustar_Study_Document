# 08. 피보나치 수열 1
def count_fibonacci(input_num):
    if input_num == 0:
        return 0
    elif input_num == 1:
        return 1
    else:
        return count_fibonacci(input_num - 1) + count_fibonacci(input_num - 2)

num_of_testcase = int(input())
for _ in range(num_of_testcase):
    print(count_fibonacci(int(input())))