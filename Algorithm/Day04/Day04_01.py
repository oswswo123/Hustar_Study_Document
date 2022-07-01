# 01. 세금징수

def tax_calculate(tax):
    num_of_coin = 0
    coin_list = [50000, 10000, 5000, 1000, 500, 100]
    for coin in coin_list:
        num_of_coin += tax // coin
        tax %= coin
    
    return num_of_coin

def main():
    num_of_testcase = int(input())
    for _ in range(num_of_testcase):
        print(tax_calculate(int(input())))

if __name__ == "__main__":
    main()