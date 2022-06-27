import collections

num_of_testcase = int(input())
for testcase in range(num_of_testcase):
    num_of_query = int(input())
    temp_queue = collections.deque(list())
    for _ in range(num_of_query):
        command = input()
        if command == "-1":
            print(temp_queue.popleft())
        else:
            temp_queue.append(command)