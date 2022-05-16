// See https://aka.ms/new-console-template for more information

// 반복문을 활용해 구구단 출력
for (int row=2; row<10; row++){
    for (int col=1; col<10; col++){
        Console.Write("{0, 2} x {1, 2} = {2, 2}  ", row, col, row*col);
    }
    Console.WriteLine();
}