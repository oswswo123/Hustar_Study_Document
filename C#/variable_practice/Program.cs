// See https://aka.ms/new-console-template for more information
// char와 string은 다름
char grade = 'A';
string grade2 = "A";
int age = 28;
Console.WriteLine(grade + grade2);
Console.WriteLine((int)age);

// Null 값을 사용하기 위해서 숫자 자료형 뒤에는 ?를 붙여야함
// int x = null;    error 발생
string aa = null;
double? d = null;
int? y = null;

// 암시적 형식 변환
double doub = 23.12;
int inte = 12345;

doub = inte;
Console.WriteLine("암시적 형식 변환 = " + doub + " " + doub.GetType());

doub = 12.34;
inte = (int)doub;
Console.WriteLine("암시적 형식 변환 = " + inte + " " + inte.GetType());

string str = "";
str = Convert.ToString(doub);
Console.WriteLine("형식 변환 = " + str + " " + str.GetType());

// input 받기
Console.Write("입력하세요 : ");
string input = Console.ReadLine();
char c = Convert.ToChar(input);
Console.WriteLine(c);