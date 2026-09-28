#loops 
#print numbers from 1 to 10
for i in range(1,11):
    print(i) 

#print numbers from 10 to 1
for i in range(10,0,-1):
     print(i)

#print even numbers from 2 to 50
for i in range(2,51,2):
     print(i)

#print odd numbers from 1 to 50
for i in range(1,51,2):
     print(i)

#multiplication of 5 to 50
for i in range(5,51,5):
     print(i)

#multiplication table
number=int(input("enter number"))
for i in range(1,11):
     print(number,"x",i,"=",number*i)

#sum of numbers from 1 to n
n=int(input("enter n:"))
total=0
for i in range(1,n+1):
     total=total+i
     print("sum:",total)

#factorial of a number
n=2
factorial=1
for i in range(1,n+1):
     factorial=factorial*i
print("factorial:",factorial)

#sum of even numbers from 2 to n
n=int(input("enter n:"))
total=0
for i in range(2,n+1,2):
     total=total+i
print("sum:",total)

#count of multiples of 3 
n=int(input("enter n:"))
count=0
for i in range(3,n+1,3):
   if i%3==0:
     count=count+1
print("count:",count)

#sum of multiples of 5 
n=int(input("enter n:"))
total=0
for i in range(1,n+1):
    if i%5==0:
     total=total+i
print("sum:",total)

#while loop
#print all even numbers from 2 to 50
i=2
while i<=50:
    print(i)
    i=i+2
pass
for i in range(1,6):
    if i==3:
        pass
    print(i)
#print all odd numbers from 2 to 50
i=3
while i<=50:
    print(i)
    i=i+2
    
#print total of number entered by user until 0 is entered
total=0
number=int(input("enter number"))
while number !=0:
     total=total+number
     number=int(input("enter a number:"))
print("total:",total)

#password checker
password=""
while password != "python123":
     password=input("enter password:")
print("login successful")

#count the number of digits in a number
number=int(input("enter number:"))
count=0
while number>0:
    number=number//10
    count=count+1
print("number of digits:",count)

#sum of digits in a number
number=int(input("enter number"))
total=0
while number > 0:
    digit=number%10
    number=number//10
    total=total+digit
print("sum of digits:",total)

#reverse a number
number=int(input("enter number"))
reverse=0
while number > 0:
    digit=number%10
    number=number//10
    reverse = reverse * 10 + digit
print("reverse:",reverse)

#check if a number is a palindrome
number=int(input("enter number"))
original=number
reverse=0
while number > 0:
    digit=number%10
    number=number//10
    reverse = reverse * 10 + digit
if original==reverse:
    print("palindrome")
else:
    print("not palindrome")

#check if a number is prime
number=int(input("enter number"))
count=0
for i in range(1,number+1):
    if number%i==0:
       count=count+1
if count==2:
    print("prime number")
else:
    print("not a prime number")

#print all prime numbers between 2 and 100
for number in range(2,101):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count=count
    if count==2:
        print(number)

#break
for i in range(1,11):

    if i==5:
        break#exit the loop
    print(i)

#continue

for i in range(1,11):
    if i==5:
        continue #skip current iteration
    print(i)

#pass
for i in range(1,6):
    if i==3:
        pass
    print(i)

#print odd numbers from 1 to 10
for i in range(1,11):
    if i %2==0:
        continue
    print(i)

#print numbers until user enters 0
while True:
    number=int(input("enter number"))
    if number==0:
        break
    print("you entered:",number)

#print numbers from 1 to 100,but skip multiples of 3 and stop at 50
for i in range(1,10):
    if i == 50:
        break
    if i % 3==0:
        continue
    print(i)

#calculate the sum of positive numbers entered by the user
total=0
while True:
    number=int(input("enter number"))
    if number<0:
        continue
    if number==0:
        break
    total=total+number
print("total:",total)

#both multiples of 3 and 5
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("first number:",i)
        break

#calculate the sum of positive numbers entered by the user
total=0
for i in range(10):
    number=int(input("enter number:"))
    if number<0:
        continue
    total=total+number

#password check with limited attempts
correct_password="python123"
for attempt in range(1,4):
    password=input("enter password")
    if password==correct_password:
        print("login successful")
        break
    print("wrong password")
else:
    print("account locked")

#find largest number among 5 numbers entered by the user
largest=None
for i in range(5):
    number=int(input("enter number:"))
    if largest is None or number >largest:
        largest=number
print("largest:",largest)

#find the smallest number among 5 numbers entered by the user
smallest=None
for i in range(5):
    number=int(input("enter number:"))
    if smallest is None or number<smallest:
        smallest=number
print("smallest:",smallest)
