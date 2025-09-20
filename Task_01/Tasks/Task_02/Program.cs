using System;
using System.Diagnostics;
using System.Text;

Console.WriteLine("Hello, Please enter the maximum number you need to write");

string? maximumNumberFromUser;
maximumNumberFromUser  = Console.ReadLine();
int maximumNumber;

if (!int.TryParse(maximumNumberFromUser, out maximumNumber) || maximumNumber < 1)
{
    Console.WriteLine("Invalid input. Please enter a positive number.");
    return;
}

string numbers ="";

Stopwatch stopwatch = Stopwatch.StartNew();


//Time complexity: O(n^2)
for (int i = 1; i <= maximumNumber; i++)
{
    numbers = $"{numbers}{i},";
}

stopwatch.Stop();

 
// Remove Comma
if (numbers.EndsWith(","))
{
    numbers = numbers.TrimEnd(',');
}

Console.WriteLine(numbers);
Console.WriteLine($"Elapsed Seconds = {stopwatch.Elapsed.TotalSeconds}");


/*
 * StringBuilder uses a dynamic char[] buffer that grows (usually doubles) only when needed. 
 * Time complexity: O(n)
 **/