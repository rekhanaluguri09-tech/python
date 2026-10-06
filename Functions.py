#basic function
def greet():
    print("Hello")
    print("Welcome to python")
greet()

#functions without parameters
def welcome():
    print("welcome to python")
welcome()
welcome()
welcome()

#function with parameters
def greet(name):
    print("Hello",name)
greet("Bhargavi")
greet("Nymi")

#multiple parameters
def add(a,b):
    print("sum:",a+b)
add(10,20)
add(50,30)

#function with return value
def add(a,b):
    return a + b
result=add(10,20)#
print(result)

#this is why return value Largest Result
def add(a,b):
    return a + b
result=add(10,20)
if result > 25:
    print("largest result")

#Function for even/odd
def check_even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
result=check_even_odd(100)
print(result)

#Function for Lagest of Two Numbers
def largest(a,b):
    if a > b:
        return a
    else:
        return b
result = largest(50,30)
print("Largest:",result)

#Function for Largest of Three Numbers
def largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
result = largest(50,30,40)
print("Largest:",result)

#Function + user input
def square(number):
    return number * number
number=int(input("enter number:"))
result=square(number)
print("square:",result)

#add two numbers taking user input
def add(a,b):
    return a+b
x=int(input("enter first number:"))
y=int(input("enter second number:"))

result=add(x,y)
print("sum =",result)

#even or odd taking user input
def check_even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
num=int(input("enter a number"))

print(check_even_odd)

#Largest of three numbers of taking user input
def largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
x=int(input("Enter a:"))
y=int(input("Enter b:"))
z=int(input("Enter c:"))
print("Largest =",largest(x,y,z))

#Largest of two numbers of taking user input
def largest(a,b):
    if a > b:
        return a
    else:
        return b
x=int(input("enter a:"))
y=int(input("Enter b:"))

print("Largest:",largest(x,y))

#Grade calculation
def find_grade(marks):
    if  marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "fail"

marks=int(input("Enter marks:"))
print("grade=",find_grade(marks))

#Function + loop
def multiplication_table(number):
    for i in range(1,11):
        print(number,"x",i,"=",number*i)

number=int(input("enter number"))
multiplication_table(number)

#sum of 1 to n
def sum_n(num):
    total = 0
    for i in range(1,num+1):
        total+=i
    return total
n=int(input("enter n:"))
print("sum =",sum_n(n))

#positive and negative
def check_positive_negative(number):
    if number>0:
        return "positive"
    elif number<0:
        return "negative"
    
n=int(input("enter n:"))
result=check_positive_negative(n)
print(result)

#Factorial of a number
def factorial(num):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
n = int(input("Enter a number:"))
print("Factorial =",factorial(num))

#sum of digits
def sum_digits(n):
    total=0
    while n > 0:
        digit = n % 10
        total += digit
        n //=10
    return total
num=int(input("Enter a number:"))
print("Sum of digits =",sum_digits(num))

#palindrome check
def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n%10
        reverse = reverse * 10 + digit
        n //=10
    if original == reverse:
        return True
    else:
        return False
num=int(input("Enter a number:"))

if is_palindrome(num):
    print("palindrome")
else:
    print("not palindrome")

#calculator using functions
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "cannot divide bv zero"
    return a/b

x=float(input("Enter first number:"))
y=float(input("Enter second number:"))

print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.divide")

choice=int(input("Enter choices:"))
if choice == 1:
    print("result =",add(x,y))
elif choice == 2:
   print("result =",subtract(x,y))
elif choice == 3:
   print("result =",multiply(x,y))
elif choice == 4:
    print("result =",divide(x,y))
else:
    print("Invalid choice")