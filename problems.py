#program 1:Display Personal Details Using Variable 
#Getting the input from user 
name=input()
age=int(input())
height=float(input())
#printing the values 
print(name)
print(age)
print(height)

#Program 2:Personalized Greeting 
name=input()
print(F"Hello,{name}!")

#Program 3:Add Two Numbers Read as Strings
#Taken the input as string 
a=input()
b=input()
#Converting the String into integer
a=int(a)
b=int(b)
#Find the sum 
total=a+b
#print the result 
print(total)

#program 4:float to integer conversion
#float:numbers with decimal value
#int:Whole numbers without any decimal or frational value 
#Reading afloat value from the user 
n=float(input)
#print the float value 
print(n)
#convert the float integer:Decimal point values will be removed 
new=int(n)
#print the result 
print(new)

#prog(ram 5:Sum using Arithmetic operator 
#reading 2 integers from the user
a=int(input())
b=int(input())
#finding the sum and printing the result 
print(a+b)

#program 6:Area of a Rectangle
#Reading input from the user
length=float(input())
breadth=float(input())
#calculating the area of a rectangle
area=length*breadth
#print the result 
print(area)

#program 7:Quotient and remainder
#user inputs
a=int(input())
b=int(input())
#find the quotient
q=a/b
#Find the remainder
r=a%b
#print the result
print(q)
print(r)
#program 8:power calculator
#reading user unit 
base=int(input(4))
exponent=int(input(2))
#calucullate the power of and print the result
print(base**exponent)

#program 9:average of three numbers
#taking 3 integer from the users
n1=int(input())
n2=int(input())
n3=int(input())
#find the total
total=n1+n2+n3
#find the average
avg=total/3#division operators /--always gives
#print the average
#print(avg)

#program 10:greater than comparision
#read 2 integer numbers from user
a=int(input())
b=int(input())

#program 11:equality check
#check whether bothe numbers are same or not 
#if the numbers are same - true
#if the numbers are different - false 
#reading the input from the user 
n1=int(input())
n2=int(input())
print(n1==n2)

#program 12:both numbers positive check 
#if the numbers is greater than O
#logic and-->if all the combining conditions are true,result is true
#reading the input from the user
n1=int(input())
n2=int(input())
print(n1>0 and n2>0)

#program 13:at least one even number
#even number:if the number is divisible by 2 (without any remainder)
#logical or -->if any one of the combining condition is true,then the result is true,
#Areithmetic operator
#/-->Division - result is in form of decimal value 
Example:13.2=6.5
#// --> floor division - result is in from of integer
Example:13.2=6

#program 14:logical not on a condition
#logical not -->reverse the result 
#true -->false
#false -->true
#reading the input from the user 
num=int(input())
print(not(num>0))

#program 15:augmented assignment operations
#read a number from the user
a=int(input())#20
a=a+5# a=20+5-->25
a=a*2# a=25*2-->50
a=a-3# a=50-3-->47
print(a)

#problem 16:exchange values of two variables
#Reading the input from the user
a=int(input())
b=int(input())
#logic 1-using temp variable
temp=a
a=b
b=temp
print(a)
print(b)
#logic 2-without using temp(3rd variable)
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#logic 3:without using temp (3rd variable)
a=a^b
b=a^b
a=a^b
print(a)
print(b)
#logic 4:without using temp (3rd variable)
#problem:it cannot handle 0
a=a*b
b=a/b
a=a/b
print(a)
print(b)
#logic 5:using python's special
#simplest way 
a,b=b,a
print(a)
print(b)

#program 17:calculate simple interest
#formula:(principle*rate*time)/100
#user inputs 
principle=float(input())#loan amount
rate=float(input())#rate of interest
time=float(input())#repayment time
#calculate interest
si=(principle*rate*time)/100
#print the result
print(si)

#program 18:temperature conversion (celsius to fahrenheit)
#formula:f=(c*9/5)+32
#read the temperature in celsius
c=float(input())
#convert the celsius to fahrenheit
f=(c*9/5)+32
print(f)

#problrem 19:check divisibility by 3 and 5
n=int(input())
print(n%3==0 and n%5==0)

#program 20:sum of digits of a two-digit number
num=int(input()) #num=48
tens=num//10     #tens=48//10=4
units=num%10     #units=48%10=8
total=tens+units #total=4+8=12
print(total)