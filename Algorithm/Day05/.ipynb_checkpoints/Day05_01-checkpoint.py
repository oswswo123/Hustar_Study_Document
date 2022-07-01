# 01. 돌다리 건너가기

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_of_cases = [0, 1, 2, 4]
        destination = int(input())
        for temp_idx in range(4, destination+1):
            num_of_cases.append(num_of_cases[temp_idx-3] % 1904101441 \
                                + num_of_cases[temp_idx-2] % 1904101441 \
                                + num_of_cases[temp_idx-1] % 1904101441)
        
        print(num_of_cases[destination] % 1904101441)

if __name__ == "__main__":
    main()