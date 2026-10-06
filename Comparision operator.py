#comparison operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#age eligibility checker
age = int(input("Enter your age:"))
print("Eligible:",age >= 18)

#pass or fail checker
marks = int(input("Enter marks"))
print("passed:", marks >= 40)

#login validation
correct_username = "admin"
correct_password = "1234"
username = input("Enter username")
password = input("Enter password")
print(username == correct_username)
print(password == correct_password)

#logical operators
age = 25
citizen = True
print(age >= 18 and citizen == True)
has_card = False
has_cash = True
print(has_card or has_cash)

#not 
is_logged_in = True
print(not is_logged_in)

#atm eligibility checker
balance = 10000
withdraw = 5000
print(withdraw > 0 and withdraw <= balance)

#student scholarship checker
marks = float(input("enter marks:"))
attendence = float(input("enter attendence:"))
eligible = marks>=85 and attendence>=75
print("scholarship eligible:",eligible)

#identity operator
a=None
print(a is None)
print(a is not None)

#bitwise operators
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b )
print(a << b)
print(a >> b)

#electric city bill calculator
units = int(input("enter electricity units:"))
rate = 6
bill = units * rate
print("electricity bill:",bill)

#travel expense calculator
travel=float(input("Travel expense:"))
food=float(input("Food expense:"))
hotel=float(input("Hotel expense"))
total=travel+food+hotel
print("Total Expense:",total)

