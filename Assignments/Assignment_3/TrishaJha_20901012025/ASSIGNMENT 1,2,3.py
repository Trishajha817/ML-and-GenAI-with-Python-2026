ASSIGNMENT 
# Program to find the area of a rectangle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth

print("Area of the rectangle =", area)

# Program to calculate Simple Interest

principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

# Program to convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

# Program to calculate the average of three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)
# Program to find the square and cube of a number

num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)
# Program to swap two numbers using a third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("First number =", a)
print("Second number =", b)
# Program to create a student's report

# Taking student details as input
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks in three subjects
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

# Calculating total marks
total = marks1 + marks2 + marks3

# Calculating percentage
percentage = total / 3

# Displaying student report
print("\n----- STUDENT REPORT -----")
print("Name :", name)
print("Roll Number :", roll_no)
print("Marks in Subject 1 :", marks1)
print("Marks in Subject 2 :", marks2)
print("Marks in Subject 3 :", marks3)
print("Total Marks :", total)
print("Percentage :", percentage, "%")


ASSIGNMENT 
# Program to find the sum of first 10 natural numbers

sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum of first 10 natural numbers =", sum)
# Program to find factorial of a number

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)
# Program to print Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    # Program to find largest among three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number =", largest)
# Student Result System

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input marks
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

# Calculate total and percentage
total = m1 + m2 + m3
percentage = total / 3

# Display grade using if-elif-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)

ASSIGNMENT 
# Function to print first 10 natural numbers

def print_natural_numbers():
    for i in range(1, 11):
        print(i)

print_natural_numbers()
# Function to calculate sum of first N natural numbers

def sum_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter N: "))
print("Sum =", sum_natural_numbers(n))
# Function to reverse a number

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

num = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(num))
# Function to count digits in a number

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))
# Function to check palindrome number

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
    # Function to generate Fibonacci series

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter number of terms: "))
fibonacci(n)
# Calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Select operation: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", subtract(num1, num2))
elif choice == 3:
    print("Result =", multiply(num1, num2))
elif choice == 4:
    print("Result =", divide(num1, num2))
else:
    print("Invalid Choice")
    # Create a file and store student details

name = input("Enter student name: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

print("Student details stored successfully.")# Read data from a file

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()
# Exception handling for division by zero

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")
    # Student class

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

s1 = Student(name, marks)

s1.display()


