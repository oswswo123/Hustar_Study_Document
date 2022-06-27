# PJ 01. 괄호 검사
num_of_testcase = int(input())
for _ in range(num_of_testcase):
    check_bracket_str = input()
    temp_stack = list()
    is_right = False
    repeat = 0
    for bracket_element in check_bracket_str:
        if bracket_element == "(" or bracket_element == "{" or bracket_element == "[":
            temp_stack.append(bracket_element)
        elif bracket_element == ")":
            try:
                if temp_stack[-1] == "(":
                    temp_stack.pop()
                else:
                    is_right = False
                    break
            except:
                is_right = False
                break
        elif bracket_element == "}":
            try:
                if temp_stack[-1] == "{":
                    temp_stack.pop()
                else:
                    is_right = False
                    break
            except:
                is_right = False
                break
        elif bracket_element == "]":
            try:
                if temp_stack[-1] == "[":
                    temp_stack.pop()
                else:
                    is_right = False
                    break
            except:
                is_right = False
                break
        else:
            pass
        repeat += 1

    if bool(temp_stack) == False and repeat == len(check_bracket_str):
        is_right = True
    else:
        is_right = False
    
    if is_right:
        print("YES")
    else:
        print("NO")