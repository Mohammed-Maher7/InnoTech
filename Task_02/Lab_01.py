# =============================
# LAB (1) – Python Basics
# =============================

# --------------------------------------
# Task 1: Accept radius of a circle and compute the area
# --------------------------------------
import math

radius = float(input("Task 1 - Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.2f}")

# --------------------------------------
# Task 2: Check if a Number is Odd or Even
# --------------------------------------
num = int(input("\nTask 2 - Enter a number to check if it's Odd or Even: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# --------------------------------------
# Task 3: Sum of three integers (sum is zero if two values are equal)
# --------------------------------------
a = int(input("\nTask 3 - Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a == b or b == c or a == c:
    total_sum = 0
else:
    total_sum = a + b + c

print(f"The result is: {total_sum}")

# --------------------------------------
# Task 4: Print the Natural Numbers Summation Pattern
# --------------------------------------
n = int(input("\nTask 4 - Enter a number for the summation pattern: "))
sum_val = 0
for i in range(1, n + 1):
    sum_val += i
    # Build the sequence as text like: 1 + 2 + ... + n
    sequence = " + ".join(str(x) for x in range(1, i + 1))
    print(f"{sequence} = {sum_val}")

# --------------------------------------
# Task 5: Check Prime Number
# --------------------------------------
num = int(input("\nTask 5 - Enter a number to check if it's prime: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is NOT a Prime Number")

# --------------------------------------
# Task 6: Display the first 16 numbers powers of 2, starting with 1
# --------------------------------------
print("\nTask 6 - First 16 powers of 2:")
value = 1
for i in range(16):
    print(value, end=" ")
    value *= 2
print()  # just to move to the next line after the loop output

# --------------------------------------
# Task 7: Print all even numbers from 1 to n using for loop
# --------------------------------------
n = int(input("\nTask 7 - Enter the range end (n): "))
print(f"Even numbers from 1 to {n}:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")
