Console.WriteLine("Hello, Please enter the maximum number you need to add");

string? maximumNumberFromUser;

maximumNumberFromUser = Console.ReadLine();

// Validate input
if (string.IsNullOrWhiteSpace(maximumNumberFromUser) || !int.TryParse(maximumNumberFromUser, out int maximumNumber))
{
    Console.WriteLine("Invalid input. Please enter a valid integer.");
    return;
}

Console.WriteLine($"Are you sure you need to get the addition up to {maximumNumber}?");


int sum = 0;

//Time complexity: O(n) 
for (int i = 1; i <= maximumNumber; i++)
{
    sum += i;
}


// Time complexity: O(c)  Where c is constant
int seriesSum = maximumNumber * (maximumNumber + 1) / 2;

Console.WriteLine($"Sum using loop = {sum}");
Console.WriteLine("Time complexity using loop = O(n)");
Console.WriteLine($"Sum using formula = {seriesSum}");
Console.WriteLine("Time complexity using formula = O(c) Where c is constant");
