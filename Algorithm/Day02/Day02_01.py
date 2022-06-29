# 01. n^k mod m 효율적으로 계산하기
def calculate_modular(n, k, m):
    if k == 0:
        return 1
    elif k == 1:
        return n % m
    else:
        x = calculate_modular(n, k//2, m)
    
        if k%2 == 0:
            # even
            return (x * x) % m
        else:
            # odd
            return (x * x * n) % m

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    n, k, m = list(map(int, input().split()))
    print(calculate_modular(n, k, m))