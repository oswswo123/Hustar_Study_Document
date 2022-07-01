# 02. 무거운 용액

def calculate_heavy_liquid(liquid_list, liquid_volumn):
    most_heavy_mass = 0
    liquid_list = sorted(liquid_list, key=lambda x:x[0])
    
    while liquid_volumn > 0:
        check_liquid = liquid_list.pop()
        if check_liquid[2] > liquid_volumn:
            most_heavy_mass += (check_liquid[0] * liquid_volumn)
            liquid_volumn = 0            
        else:
            most_heavy_mass += (check_liquid[0] * check_liquid[2])
            liquid_volumn -= check_liquid[2]            
    
    return int(most_heavy_mass)

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        num_of_liquid, liquid_volumn = tuple(map(int, input().split()))
        liquid_list = list()
        
        for _ in range(num_of_liquid):
            mass, volumn = tuple(map(int, input().split()))
            liquid_list.append((mass/volumn, mass, volumn))
        
        print(calculate_heavy_liquid(liquid_list, liquid_volumn))

if __name__ == "__main__":
    main()