# ============================================
# LAB (2) - Python Fundamentals
# ============================================

# --------------------------------------------
# BASICS
# --------------------------------------------

# Task 1: Convert inches to centimeters
length_in_inches = float(input("Task 1 - Enter length in inches: "))
length_in_cm = length_in_inches * 2.54
print(f"Length in centimeters: {length_in_cm:.2f} cm")

# Task 2: Convert Celsius to Fahrenheit
celsius = float(input("\nTask 2 - Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")

# Task 3: Volume of a sphere
import math
radius = float(input("\nTask 3 - Enter radius of the sphere: "))
volume = (4/3) * math.pi * radius**3
print(f"Volume of the sphere: {volume:.2f}")

# Task 4: Employee gross and net pay
gross_pay = float(input("\nTask 4 - Enter gross pay: "))
tax = gross_pay * 0.20
net_pay = gross_pay - tax
print(f"Net pay after 20% tax: {net_pay:.2f}")

# Task 5: Print numbers 1-10
print("\nTask 5 - Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# Task 6: Accept numbers until negative number is entered
print("\nTask 6 - Enter numbers (negative to stop):")
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number entered. Stopping.")
        break

# Task 7: Identify the range of an integer
num = int(input("\nTask 7 - Enter an integer to find its range: "))
if 0 <= num <= 10:
    print("Range 1: 0 to 10")
elif 11 <= num <= 20:
    print("Range 2: 11 to 20")
elif 21 <= num <= 30:
    print("Range 3: 21 to 30")
elif 31 <= num <= 40:
    print("Range 4: 31 to 40")
else:
    print("Number is out of the defined ranges.")

# --------------------------------------------
# STRINGS
# --------------------------------------------

# Task 1: Reverse a string
text = input("\nString Task 1 - Enter a string to reverse: ")
print("Reversed string:", text[::-1])

# Task 2: Count upper and lower case letters
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

sample_str = input("\nString Task 2 - Enter a string: ")
u, l = count_case(sample_str)
print(f"Upper case letters: {u}, Lower case letters: {l}")

# Task 3: Check if string is palindrome
pal_str = input("\nString Task 3 - Enter a string to check palindrome: ")
if pal_str.replace(" ", "").lower() == pal_str.replace(" ", "").lower()[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# --------------------------------------------
# LISTS
# --------------------------------------------

# Task 1: Distinct elements from a list
def unique_list(lst):
    return list(set(lst))

print("\nList Task 1 - Unique List:")
print(unique_list([1, 2, 3, 3, 3, 4, 5]))

# Task 2: Print even numbers from list
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print("\nList Task 2 - Even numbers:", even_numbers([1,2,3,4,5,6,7,8,9]))

# Task 3: Find kth largest element in a list
def kth_largest(lst, k):
    return sorted(lst, reverse=True)[k-1]

print("\nList Task 3 - 2nd largest:", kth_largest([10, 20, 4, 45, 99], 2))

# Task 4: Check if a list is a palindrome
def is_list_palindrome(lst):
    return lst == lst[::-1]

print("\nList Task 4 - Palindrome list:", is_list_palindrome([1,2,3,2,1]))

# Task 5: Shopping list of 10 items
shopping_list = ["Milk", "Eggs", "Bread", "Apples", "Butter", "Cheese", "Tea", "Sugar", "Rice", "Flour"]
print("\nList Task 5 - Shopping List:", shopping_list)
print("Item 2:", shopping_list[1])
print("Item 8:", shopping_list[7])

# Task 6: Insert item into list
shopping_list.insert(5, "Honey")
print("Updated Shopping List:", shopping_list)

# --------------------------------------------
# DICTIONARY
# --------------------------------------------

# Task 1: Sort dictionary by value
my_dict = {"a": 5, "b": 2, "c": 8}
print("\nDict Task 1 - Ascending sort:", dict(sorted(my_dict.items(), key=lambda x: x[1])))
print("Descending sort:", dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)))

# Task 2: Check if key exists
key = "a"
print("\nDict Task 2 - Key exists?" , key in my_dict)

# Task 3: Iterate over dictionary
print("\nDict Task 3 - Iterate:")
for k, v in my_dict.items():
    print(k, v)

# Task 4: Generate dictionary of squares
n = 5
square_dict = {x: x**2 for x in range(1, n+1)}
print("\nDict Task 4 - Squares:", square_dict)

# Task 5: Add employee data
employees = {}
employees[101] = {"name": "John", "dept": "HR"}
employees[102] = {"name": "Jane", "dept": "IT"}
print("\nDict Task 5 - Employees:", employees)

# --------------------------------------------
# FUNCTIONS
# --------------------------------------------

# Task 1: Function to square a number
def square(num):
    return num ** 2

print("\nFunction Task 1 - Square:", square(4))

# Task 2: Return largest of two numbers
def largest(a, b):
    return a if a > b else b

print("Function Task 2 - Largest:", largest(10, 25))

# --------------------------------------------
# OOP
# --------------------------------------------

# Task 1: Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("\nOOP Task 1 - Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

# Task 2: Person class
class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year
    def age(self, current_year):
        return current_year - self.birth_year

p = Person("Ali", "Egypt", 2000)
print("\nOOP Task 2 - Person Age:", p.age(2025))

# Task 3: Calculator class
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "Error"

calc = Calculator()
print("\nOOP Task 3 - Calculator Add:", calc.add(10, 5))

# Task 4: Shape superclass with subclasses
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side

sq = Square(4)
print("\nOOP Task 4 - Square Area:", sq.area())
print("Square Perimeter:", sq.perimeter())
