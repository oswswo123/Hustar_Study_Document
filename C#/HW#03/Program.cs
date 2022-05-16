// See https://aka.ms/new-console-template for more information

// 계산기 프로그램 작성
// 객체를 선언해서 프로그램 작성
// 나눗셈에서 0으로 나누어지면 안된다.
// 정수, 실수 연산
// 사칙연산 나눗셈의 경우 몫과 나머지 둘 다 측정 가능
// 거듭제곱, 절대값 기능 추가
// 결과는 입력받은 숫자도 보이도록
/*
Calculator cal = new Calculator();
String? command = null;
String buffer1, buffer2;
Boolean isInteger = true;
int il_oper = 0, ir_oper = 0;
double fl_oper = 0, fr_oper = 0;

while(command != "q"){
        Console.Write("isInteger? (y/n) (q : quit): ");
        command = Console.ReadLine().ToLower();
        if(command == "y") { isInteger = true; }
        else if (command == "n") { isInteger = false; }
        else if (command == "q") { continue; }
        else {
            Console.WriteLine("Invalid input.");
            continue;
        }

        Console.Write("command = (+, -, *, /, %, ^, abs) (q : quit)\ninput command : ");
        command = Console.ReadLine().ToLower();
        if(command == "q") { continue; }

        Console.Write("first number : ");
        buffer1 = Console.ReadLine();
        if(isInteger){ il_oper = Convert.ToInt32(buffer1); }
        else { fl_oper = Convert.ToDouble(buffer1); }
        
        if(command != "abs"){
            Console.Write("second number : ");
            buffer2 = Console.ReadLine();
            if(isInteger){ ir_oper = Convert.ToInt32(buffer2); }
            else { fr_oper = Convert.ToDouble(buffer2); }
        }

        switch(command){
            case "+":
                if(isInteger) { cal.CalAdd(il_oper, ir_oper); }
                else { cal.CalAdd(fl_oper, fr_oper); }
                break;
            case "-":
                if(isInteger) { cal.CalSub(il_oper, ir_oper); }
                else { cal.CalSub(fl_oper, fr_oper); }
                break;
            case "*":
                if(isInteger) { cal.CalMul(il_oper, ir_oper); }
                else { cal.CalMul(fl_oper, fr_oper); }
                break;
            case "/":
                if(isInteger) { cal.CalDiv(il_oper, ir_oper); }
                else { cal.CalDiv(fl_oper, fr_oper); }
                break;
            case "%":
                if(isInteger) { cal.CalRem(il_oper, ir_oper); }
                else { cal.CalRem(fl_oper, fr_oper); }
                break;
            case "^":
                if(isInteger) { cal.CalSqu(il_oper, ir_oper); }
                else { cal.CalSqu(fl_oper, fr_oper); }
                break;
            case "abs":
                if(isInteger) { cal.CalAbs(il_oper); }
                else { cal.CalAbs(fl_oper); }
                break;
            default:
                Console.WriteLine("Invalid input.");
                break;
            }        
        }

public class Calculator{
    public Calculator() { }
    
    public int CalAdd(int l_oper, int r_oper) {
        Console.WriteLine(l_oper + " + " + r_oper + " = " + (l_oper+r_oper));
        return l_oper + r_oper;
    }
    public double CalAdd(double l_oper, double r_oper) {
        Console.WriteLine(l_oper + " + " + r_oper + " = " + (l_oper+r_oper));
        return l_oper + r_oper;
    }
    public int CalSub(int l_oper, int r_oper) {
        Console.WriteLine(l_oper + " - " + r_oper + " = " + (l_oper-r_oper));
        return l_oper - r_oper;
    }
    public double CalSub(double l_oper, double r_oper) {
        Console.WriteLine(l_oper + " - " + r_oper + " = " + (l_oper-r_oper));
        return l_oper - r_oper;
    }
    public int CalMul(int l_oper, int r_oper) {
        Console.WriteLine(l_oper + " * " + r_oper + " = " + (l_oper*r_oper));
        return l_oper * r_oper;
    }
    public double CalMul(double l_oper, double r_oper) {
        Console.WriteLine(l_oper + " * " + r_oper + " = " + (l_oper*r_oper));
        return l_oper * r_oper;
    }
    public int CalDiv(int l_oper, int r_oper) {
        if (r_oper == 0){
            Console.WriteLine("Cannot Divide Zero.");
            return -1;
        }
        Console.WriteLine(l_oper + " / " + r_oper + " = " + (l_oper/r_oper));
        return l_oper / r_oper;
    }
    public double CalDiv(double l_oper, double r_oper) {
        if (r_oper == 0){
            Console.WriteLine("Cannot Divide Zero.");
            return -1;
        }
        Console.WriteLine(l_oper + " / " + r_oper + " = " + (l_oper/r_oper));
        return l_oper / r_oper;
    }
    public int CalRem(int l_oper, int r_oper) {
        Console.WriteLine(l_oper + " % " + r_oper + " = " + (l_oper%r_oper));
        return l_oper % r_oper;
    }
    public double CalRem(double l_oper, double r_oper) {
        Console.WriteLine(l_oper + " % " + r_oper + " = " + (l_oper%r_oper));
        return l_oper % r_oper;
    }
    public int CalSqu(int l_oper, int r_oper) {
        Console.WriteLine(l_oper + " ^ " + r_oper + " = " + Math.Pow(l_oper, r_oper));
        return (int)Math.Pow(l_oper, r_oper);
    }
    public double CalSqu(double l_oper, double r_oper) {
        Console.WriteLine(l_oper + " ^ " + r_oper + " = " + Math.Pow(l_oper, r_oper));
        return Math.Pow(l_oper, r_oper);
    }
    public int CalAbs(int l_oper) {
        Console.WriteLine("|" + l_oper + "|" + " = " + Math.Abs(l_oper));
        return (int)Math.Abs(l_oper);
    }
    public double CalAbs(double l_oper) {
        Console.WriteLine("|" + l_oper + "|" + " = " + Math.Abs(l_oper));
        return Math.Abs(l_oper);
    }
}
*/


// 도서 대여 프로그램
// 사람에 대한 클래스 작성(len(attribute) >= 4, len(method) >= 2)
// 입력 -> 검색
Person[] crowd = new Person[5];

crowd[0] = new Person("윤병남", 33, true, "파이썬 기초");
crowd[1] = new Person("김동준", 29, false);
crowd[2] = new Person("김민호", 27, true, "자연어 처리 입문");
crowd[3] = new Person("강나현", 26, true, "GPT-3 사용법");
crowd[4] = new Person("이병화", 26, false);

Console.WriteLine("1:이름으로 조회, 2:나이로 조회, 3:대여상태로 조회, 4:대여중인 책이름으로 조회");
Console.Write("조회 정보 : ");
int inputcommand = Convert.ToInt32(Console.ReadLine());

switch(inputcommand){
    case 1:
        Console.Write("이름을 입력하세요 : ");
        String inputname = Console.ReadLine();
        for(int idx=0; idx<crowd.Length; idx++){
            if(crowd[idx].GetName() == inputname) { crowd[idx].Display(); }
        }
        break;
    case 2:
        Console.Write("나이를 입력하세요 : ");
        int inputage = Convert.ToInt32(Console.ReadLine());
        for(int idx=0; idx<crowd.Length; idx++){
            if(crowd[idx].GetAge() == inputage) { crowd[idx].Display(); }
        }
        break;
    case 3:
        Boolean isRent;
        Console.Write("대여상태를 입력하세요 (T/F) : ");
        String isRentStr = Console.ReadLine().ToLower();
        if(isRentStr == "t"){ isRent = true; }
        else if(isRentStr=="f"){ isRent = false; }
        else{ 
            Console.WriteLine("Invalid Input.");
            break;
        }
        for(int idx=0; idx<crowd.Length; idx++){
            if(crowd[idx].GetIsRent() == isRent) { crowd[idx].Display(); }
        }
        break;
    case 4:
        Console.Write("대여할 책 이름을 입력하세요 : ");
        String inputbookname = Console.ReadLine();
        for(int idx=0; idx<crowd.Length; idx++){
            if(crowd[idx].GetRentBook() == inputbookname) { crowd[idx].Display(); }
        }
        break;
    default:
        Console.WriteLine("Invalid Input.");
        break;
}
public class Person{
    private String name, rentBook;
    private int age;
    private Boolean isRent;
    public Person(String name="noname", int age=0, Boolean isRent=false, String rentBook="none"){
        this.SetName(name);
        this.SetAge(age);
        this.SetIsRent(isRent);
        this.SetRentBook(rentBook);
    }

    public void Display(){
        Console.WriteLine("이름 : {0}", this.GetName());
        Console.WriteLine("나이 : {0}", this.GetAge());
        Console.WriteLine("대여상태 : {0}", this.GetIsRent());
        if(this.GetIsRent()) { Console.WriteLine("대여 책 이름 : {0}", this.GetRentBook()); }
    }
    public void BookRent(String bookname){
        if(isRent){
            Console.WriteLine("이미 대여중인 책이 있습니다.");
            return;
        }

        SetIsRent(true);
        SetRentBook(bookname);
        Console.WriteLine("이름 : {0}", this.GetName());
        Console.WriteLine("책 {0}을 빌렸습니다.", this.GetRentBook());
    }
    public void BookReturn(){
        if(!isRent){
            Console.WriteLine("대여중인 책이 없습니다.");
            return;
        }
        Console.WriteLine("이름 : {0}", this.GetName());
        Console.WriteLine("책 {0}을 반납했습니다.", this.GetRentBook());
        SetIsRent(false);
        SetRentBook("none");        
    }
    public void CheckRent(){
        Console.WriteLine("이름 : {0}", this.GetName());
        if(this.GetIsRent()){
            Console.WriteLine("대여중인 책 : {0}", this.GetRentBook());
        }
        else{
            Console.WriteLine("현재 도서 대여 상태가 아닙니다.");
        }
    }

    public String GetName() { return this.name; }
    public void SetName(String name) { this.name = name; }
    public int GetAge() { return this.age; }
    public void SetAge(int age) { this.age = age; }
    public Boolean GetIsRent() { return this.isRent; }
    public void SetIsRent(Boolean isRent) { this.isRent = isRent; }
    public String GetRentBook() { return this.rentBook; }
    public void SetRentBook(String rentBook) { this.rentBook = rentBook; }
}