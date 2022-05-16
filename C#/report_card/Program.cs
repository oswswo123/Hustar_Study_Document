// See https://aka.ms/new-console-template for more information

// 그냥 총점 평균 출력
/*
int korScore = 100;
int engScore = 90;
int metScore = 97;

int sumScore = korScore + engScore + metScore;
float meanScore = (float)sumScore / 3;

Console.WriteLine("총점 : {0}", sumScore);
Console.WriteLine("평균 : {0:0.00}", meanScore);
*/

// 입력 받아서 총점 평균 출력
/*
Console.Write("국어 점수 : ");
String? buffer = Console.ReadLine();
int korScore = Convert.ToInt32(buffer);
Console.Write("수학 점수 : ");
buffer = Console.ReadLine();
int metScore = Convert.ToInt32(buffer);
Console.Write("영어 점수 : ");
buffer = Console.ReadLine();
int engScore = Convert.ToInt32(buffer);

int sumScore = korScore + engScore + metScore;
float meanScore = (float)sumScore / 3;

Console.WriteLine("총점 : {0}", sumScore);
Console.WriteLine("평균 : {0:0.00}", meanScore);
*/

// 조건문 추가(평균이 90점 이상이면 학점이 A, 80~90이면 B ... )
/*
Console.Write("국어 점수 : ");
String? buffer = Console.ReadLine();
int korScore = Convert.ToInt32(buffer);
Console.Write("수학 점수 : ");
buffer = Console.ReadLine();
int metScore = Convert.ToInt32(buffer);
Console.Write("영어 점수 : ");
buffer = Console.ReadLine();
int engScore = Convert.ToInt32(buffer);

int sumScore = korScore + engScore + metScore;
float meanScore = (float)sumScore / 3;
char? grade = null;

// if (meanScore >= 90){
//     grade = 'A';
// } else if (meanScore >= 80){
//     grade = 'B';
// } else if (meanScore >= 70){
//     grade = 'C';
// } else if (meanScore >= 60){
//     grade = 'D';
// } else {
//     grade = 'F';
// }

switch((int)meanScore/10){
    case 10:
    case 9:
        grade = 'A';
        break;
    case 8:
        grade = 'B';
        break;
    case 7:
        grade = 'C';
        break;
    case 6:
        grade = 'D';
        break;
    case 5:
    case 4:
    case 3:
    case 2:
    case 1:
    case 0:
        grade = 'F';
        break;
    default:
        Console.Write("Invalid Input!\n");
        break;
}

Console.WriteLine("총점 : {0}", sumScore);
Console.WriteLine("평균 : {0:0.00}", meanScore);
Console.WriteLine("학점 : {0}", grade);
*/

// 반복문 추가 (학생 5명의 국영수 점수 입력받아서 평균으로 학점 구하기)

int numOfStudent = 5;

int korScore;
int metScore;
int engScore;
char grade;
float[] meanScores = new float[numOfStudent];
char[] grades = new char[numOfStudent];
String? buffer = null;

for(int idx=0; idx<numOfStudent; idx++){
    Console.Write("국어 점수 : ");
    buffer = Console.ReadLine();
    korScore = Convert.ToInt32(buffer);
    Console.Write("수학 점수 : ");
    buffer = Console.ReadLine();
    metScore = Convert.ToInt32(buffer);
    Console.Write("영어 점수 : ");
    buffer = Console.ReadLine();
    engScore = Convert.ToInt32(buffer);

    int sumScore = korScore + engScore + metScore;
    float meanScore = (float)sumScore / 3;
    meanScores[idx] = meanScore;

    if (meanScore >= 90){
        grade = 'A';
    } else if (meanScore >= 80){
        grade = 'B';
    } else if (meanScore >= 70){
        grade = 'C';
    } else if (meanScore >= 60){
        grade = 'D';
    } else {
        grade = 'F';
    }

    grades[idx] = grade;
}

for(int idx=0; idx<numOfStudent; idx++){
    Console.WriteLine("Person[{0}]", idx);
    Console.Write("평균 : {0:0.00}\t", meanScores[idx]);
    Console.WriteLine("학점 : {0}\n", grades[idx]);
}