// See https://aka.ms/new-console-template for more information

// Void 함수 실습
/*
String testString = "Hello, Wolrd!";
Show(testString);

// 함수
void Show(String msg){
    Console.WriteLine(msg);
    return;
}
*/

// Return type이 있는 함수
/*
String testString = "Hello, World!";
Boolean isShow = Show(testString);
Console.WriteLine(isShow);

Boolean Show(String msg){
    Console.WriteLine(msg);
    return true;
}
*/

// 두 수의 합을 구하는 함수와
// 함수를 사용하여 큰 값과 작은 값, 절댓값 구하기
/*
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
*/

// System argument 활용
/*
SumNumber(args[0], args[1]);

void SumNumber(String first, String second){
    int l_oper, r_oper;
    l_oper = Convert.ToInt32(first);
    r_oper = Convert.ToInt32(second);
    Console.WriteLine(l_oper + r_oper);
    return;
}
*/

// Math Class
/*
Console.WriteLine(Math.Pow(2, 10));
Console.WriteLine(Math.Max(3, 5));
*/

// 구조체
/*
BusinessCard bc;

bc.name = "SeungHwan Oh";
bc.tel = "010-1111-2222";
bc.email = "aaaaa@gmail.com";
bc.id = 0;
Console.WriteLine("이름 : {0}\n전화번호 : {1}\n이메일 : {2}\nID : {3}"
                    ,bc.name, bc.tel ,bc.email ,bc.id);
struct BusinessCard{
    public String name;
    public String tel;
    public String email;
    public int id;
}
*/

// DateTime : 시간 및 날짜 정보 받는 구조체
// TimeSpan : 시간, 날짜 간격에 대한 정보를 제공 해주는 구조체
// Char 구조체 : 문자에 대한 정보
/*
char a = 'A';
char b = 'a';

if(Char.IsUpper(a)){
    Console.WriteLine("{0}은 대문자", a);
}

if(Char.IsLower(b)){
    Console.WriteLine("{0}은 소문자", b);
}
*/

// static 함수
/*
Example.StaticMethod();
Example ins = new Example();
ins.InstanceMethod();
public class Example{
    public static void StaticMethod(){
        Console.WriteLine("static method");
    }

    public void InstanceMethod(){
        Console.WriteLine("Instance Method");
    }
}
*/

// random 함수
/*
Random random = new Random();
Console.WriteLine(random.Next());
Console.WriteLine(random.Next(10));
Console.WriteLine(random.Next(1, 20));
*/