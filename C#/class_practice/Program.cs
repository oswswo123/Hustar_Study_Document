// See https://aka.ms/new-console-template for more information

// 클래스 연습
/*
Dog dog = new Dog();
Dog dog2 = new Dog(2, 1, 1, 2);
dog.Bark();
dog.Display();
dog2.Display();
Console.WriteLine("Eyes : {0}", dog2.GetEyes());
dog2.SetEyes(10);
Console.WriteLine("Eyes : {0}", dog2.GetEyes());
class Dog{
    private int eyes, nose, mouse, ears;

    public Dog(int eyes=0, int nose=0, int mouse=0, int ears=0){
        this.eyes = eyes;
        this.nose = nose;
        this.mouse = mouse;
        this.ears = ears;
    }
    public void Bark(){
        Console.WriteLine("멍멍");
    }
    public void Display(){
        Console.WriteLine("eyes = {0}", this.GetEyes());
        Console.WriteLine("nose = {0}", this.GetNose());
        Console.WriteLine("mouse = {0}", this.GetMouse());
        Console.WriteLine("ears = {0}", this.GetEars());
    }
    public int GetEyes() { return this.eyes; }
    public void SetEyes(int eyes) { this.eyes = eyes; }
    
    public int GetNose() { return this.nose; }
    public void SetNose(int nose) { this.nose = nose; }
    
    public int GetMouse() { return this.mouse; }
    public void SetMouse(int mouse) { this.mouse = mouse; }
    
    public int GetEars() { return this.ears; }
    public void Setears(int ears) { this.ears = ears; }
}
*/

// 사람 클래스 만들기
/*
Person bh = new Person("병화", 24, 183, 73, true);
bh.Display();
bh.Walk(2);
bh.Sleep(3);
class Person{
    private String name;
    private int age, weight, height;
    private Boolean isMale;
    
    public Person(String name="No Name", int age=0, int weight=0, int height=0, Boolean isMale=true){
        this.SetName(name);
        this.SetAge(age);
        this.SetWeight(weight);
        this.SetHeight(height);
        this.SetIsMale(isMale);
    }

    public String GetName() { return this.name; }
    public void Setname(String name) { this.name = name; }
    public int GetAge() { return this.age; }
    public void SetAge(int age) { this.age = age; }
    public int GetWeight() { return this.weight; }
    public void SetWeight(int weight) { this.weight = weight; }
    public int GetHeight() { return this.height; }
    public void SetHeight(int height) { this.height = height; }
    public Boolean GetIsMale() { return this.isMale; }
    public void SetIsmale(Boolean isMale) { this.isMale = isMale; }

    public void Display(){
        Console.WriteLine("이름 : {0}", this.GetName());
        Console.WriteLine("나이 : {0}", this.GetAge());
        Console.WriteLine("몸무게 : {0}", this.GetWeight());
        Console.WriteLine("신장 : {0}", this.GetHeight());
        Console.WriteLine("성별 : {0}", this.GetIsMale() ? "남자" : "여자");
    }
    public void Sleep(int hour=0){
        for (int repet=0; repet<hour; repet++) { Console.WriteLine("zzz"); }
        Console.WriteLine("기상 !");
    }
    public void Walk(int step=0){
        for(int repet=0; repet<step; repet++) { Console.WriteLine("터벅"); }
        Console.WriteLine("걷기 끝");
    }
}
*/

// 상속

BullDog bd = new BullDog();
bd.Display();
public class Dog{
    private int eyes, nose, mouse, ears;

    public Dog(int eyes=0, int nose=0, int mouse=0, int ears=0){
        this.SetEyes(eyes);
        this.SetNose(nose);
        this.SetMouse(mouse);
        this.SetEars(ears);
    }
    public void Bark(){
        Console.WriteLine("멍멍");
    }
    public void Display(){
        Console.WriteLine("eyes = {0}", this.GetEyes());
        Console.WriteLine("nose = {0}", this.GetNose());
        Console.WriteLine("mouse = {0}", this.GetMouse());
        Console.WriteLine("ears = {0}", this.GetEars());
    }
    public int GetEyes() { return this.eyes; }
    public void SetEyes(int eyes) { this.eyes = eyes; }
    
    public int GetNose() { return this.nose; }
    public void SetNose(int nose) { this.nose = nose; }
    
    public int GetMouse() { return this.mouse; }
    public void SetMouse(int mouse) { this.mouse = mouse; }
    
    public int GetEars() { return this.ears; }
    public void SetEars(int ears) { this.ears = ears; }
}

public class BullDog : Dog{
    private String kind;
    public BullDog(int eyes=0, int nose=0, int mouse=0, int ears=0, String kind="불독") : base(eyes, nose, mouse, ears){
        this.SetKind(kind);
    }
    
    new public void Display(){
        base.Display();
        Console.WriteLine("kind = {0}", this.GetKind());
    }
    public String GetKind() { return this.kind; }
    public void SetKind(String kind) { this.kind = kind; }
}