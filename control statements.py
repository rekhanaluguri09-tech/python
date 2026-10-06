#if statement:when we used we want to execute only one condition
if 28>=18:
    print("eligible for voting")
#divisible by 5
number=int(input("enter a number"))
if number%5==0:
    print("divisible by 5")

#temperature check 
temperature=float(input("enter temperature"))

if temperature>40:
    print("high temperature")

#if-else statement:two coditions
if 20>=29:
    print("eligible for voting")
else:
    print("not eligible")

age=18
if age>=20:
    print("eligible")
else:
    print("not eligible")

#pass or fail
if number>=40:
    print("pass")
else:
    print("fail")

#even or odd
num=int(input("enter a number:"))
if num%2==0:
    print("even")
else:
    print("odd")

#positive or negative
num=int(input("enter a number:"))
if num>0:
    print("positive")
else:
    print("negative")

#number is greater than 100
if number>100:
    print(" number is greater than 100")
else:
    print("number is not greater than 100")

#largest of two numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a>b:
    print("largest:",a)
elif b>a:
    print("largest:",b)
else:
    print("both are equal")

#largest of three numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>=b and a>=c:
    print("largest:",a)
elif b>=a and b>=c:
    print("largest:",b)
else:
    print("largest:",c)

#day number
day=int(input("enter day number"))

if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("invalid day number")

#positive,negative or zero
num=int(input("enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
operator=input("Enter operator(+,-,*,/):")
if operator=="+":
    print("Result:",a+b)
elif operator=="-":
    print("Result:",a-b)
elif operator=="*":
    print("Result:",a*b)
elif operator=="/":
    if b!=0:
        print("Result:",a/b)
    else:
        print("cannot divide by zero")
else:
    print("invalid operator")

username=input("enter username:")
password=input("enter password:")
if username=="admin":
    if password=="1234":
        print("login successful")
    else:
        print("wrong password")
else:
    print("wrong username")

marks=int(input("enter marks:"))
attendence=float(input("enter attendence percentage:"))
if marks>=40:
    if attendence>=75:
        print("eligible")
    else:
        print("not eligible due to attendence")
else:
    print("fail")

#Bank withdrawal
balance=float(input("enter balance:"))
amount=float(input("enter amount to withdraw:"))
if amount>=0:
   if amount<=balance:
    balance-=amount
    print("withdrawal successful:")
    print("remaining balance:",balance)
   else:
    print("insufficient balance")
else:
    print("invalid amount")

age=int(input("enter age:"))
test=input("did you pass the driving test? (yes/no):")
if age>=18:
    if test=="yes":
        print("license can be issued")
    else:
        print("pass the driving test first")
else:
    print("not eligible due to age")
