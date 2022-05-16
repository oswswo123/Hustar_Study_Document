// See https://aka.ms/new-console-template for more information
// 두 수의 합을 구하는 함수와
// 함수를 사용하여 큰 값과 작은 값, 절댓값 구하기
int SumNumber(int l_oper, int r_oper){ return l_oper + r_oper; }
int MaxNumber(int l_oper, int r_oper){ return (l_oper > r_oper) ? l_oper : r_oper;}
int MinNumber(int l_oper, int r_oper){ return (l_oper < r_oper) ? l_oper : r_oper;}
int AbsNumber(int inputNumber) { return (inputNumber > 0) ? inputNumber : (inputNumber * -1);}

int firNum, secNum;
Console.Write("첫번째 수 : ");
firNum = Convert.ToInt32(Console.ReadLine());   // input이 null이면 0 return
Console.Write("두번째 수 : ");
secNum = int.Parse(Console.ReadLine());     // input이 null이면 error

Console.WriteLine("합 : " + SumNumber(firNum, secNum));
Console.WriteLine("큰 수 : " + MaxNumber(firNum, secNum));
Console.WriteLine("작은 수 : " + MinNumber(firNum, secNum));
Console.WriteLine("첫번째 수 절대값 : " + AbsNumber(firNum));
Console.WriteLine("두번째 수 절대값 : " + AbsNumber(secNum));

// 로또 번호 생성기
// 1 ~ 45 사이의 랜덤값
// 로또 번호의 개수는 6개
// 로또 번호 6개는 마지막에 한번에 출력
// 중복된 수는 존재 불가
int[] lotto = new int[6];
Random lotto_random = new Random();
Boolean isPass = true;

int tempNumber = lotto_random.Next(1,45);
lotto[0] =  tempNumber;
for(int idx=1; idx<lotto.Length; idx++){
    while(isPass){        
        tempNumber = lotto_random.Next(1, 45);
        isPass = false;
        for(int test_idx=0; test_idx<idx; test_idx++){
            if(tempNumber==lotto[test_idx]){
                isPass = true;
            }
        }
    }

    lotto[idx] = tempNumber;
    isPass = true;
}

Console.Write("로또 번호 : ");
for(int idx=0; idx<lotto.Length; idx++){
    Console.Write(lotto[idx] + " ");
}
Console.WriteLine();

// 가위바위보 게임
// 사용자가 가위 바위 보 입력
// 컴퓨터가 가위 바위 보 랜덤으로 생성
// 승 패 출력
Console.Write("주먹 = 0, 가위 = 1, 보자기 = 2\n입력 : ");
int userState = Convert.ToInt32(Console.ReadLine());

String[] rsp = new String[3];
rsp[0] = "주먹";    rsp[1] = "가위";    rsp[2] = "보자기";
Random rsp_random = new Random();
int comState = rsp_random.Next(3);
int matchResult = userState - comState;

Console.WriteLine("플레이어 : " + rsp[userState]);
Console.WriteLine("컴퓨터 : " + rsp[comState]);
switch(matchResult){
    // draw
    case 0:
        Console.WriteLine("승부 결과 : 무승부");
        break;
    // user win
    case -1:
    case 2:
        Console.WriteLine("승부 결과 : 플레이어 승리");
        break;
    // computer win
    case 1:
    case -2:
        Console.WriteLine("승부 결과 : 플레이어 패배");
        break;
    default:
        Console.WriteLine("Invalid input!!");
        break;
}