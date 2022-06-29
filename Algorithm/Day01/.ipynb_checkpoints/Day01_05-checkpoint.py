# 05. 스택 구현하기
num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    query_length = int(input())
    test_list = list()
    for _ in range(query_length):
        command = input()
        if command == "-1":
            print(test_list.pop())
        else:
            test_list.append(command)