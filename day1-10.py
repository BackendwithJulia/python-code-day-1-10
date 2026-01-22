# Day 8: Temperature Converter
# Challenge
# Convert Celsius to Fahrenheit.
# Display the converted value.
# Stretch
# Add Fahrenheit to Celsius conversion.

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose an option (1–3): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")

    elif choice == "3":
        print("Exiting Temperature Converter.")
        break
    else:
        print("Invalid choice. Try again.")

# Day 9: Basic Menu Program
# Challenge
# Display a menu:
# Check age
# Calculator
# Exit
# Perform actions based on user choice.
# Stretch
# Loop the menu until the user exits.

while True:
    print("\nMain Menu")
    print("1. Check Age")
    print("2. Calculator")
    print("3. Exit")

    choice = input("Select an option (1–3): ")

    if choice == "1":
        age = int(input("Enter your age: "))
        if age < 13:
            print("You are a child")
        elif age < 18:
            print("You are a teenager")
        else:
            print("You are an adult")

    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Addition: {num1 + num2}")
        print(f"Subtraction: {num1 - num2}")
        print(f"Multiplication: {num1 * num2}")
        if num2 != 0:
            print(f"Division: {num1 / num2}")
        else:
            print("Division by zero not allowed")

    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid option. Try again.")

# Day 10: Mini Project – Daily Utility App
# Challenge
# Combine at least three previous challenges into one program.
# Use conditions and user input.
# Stretch
while True:
    print("\nDaily Utility App")
    print("1. Age Checker")
    print("2. Calculator")
    print("3. Temperature Converter")
    print("4. Exit")

    choice = input("Choose an option (1–4): ")

    if choice == "1":
        age = int(input("Enter your age: "))
        if age < 13:
            print("Child")
        elif age < 18:
            print("Teenager")
        else:
            print("Adult")

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Add: {a + b}")
        print(f"Subtract: {a - b}")
        print(f"Multiply: {a * b}")
        print("Divide:", a / b if b != 0 else "Not allowed")

    elif choice == "3":
        temp = float(input("Enter Celsius: "))
        print(f"Fahrenheit: {(temp * 9/5) + 32}")

    elif choice == "4":
        print("Thank you for using the Daily Utility App.")
        break
    else:
        print("Invalid choice.")

                 
#             solution
# days 1–10: Python Basics (Daily Challenges)
# Day 1: Hello World & Variables
# Challenge
# Write a program that prints a welcome message.
def greeting():
    print("hello welcome to the 100 days of code in your preferred programming language")
greeting()
# Ask for the user’s name and age.
User = input('Enter your name and age: ')
print (User)

def user():
    print (message)

message = input('Enter your name and age: ') 
user()
# Print a personalised greeting
def  personalisedGreeting():
    print(message)

message = "hello lovelys,whats up beautiful people"
personalisedGreeting()


#      day2: Simple Calculator
# Challenge
# Build a calculator that takes two numbers.
# Perform addition, subtraction, multiplication, and division.
# Display all 
 
def addition(a,b):
    print("we are adding two numbers{a,b}")
    return (a+b)

add = addition(7,8)
print(add)

def subtraction(a,b):
    print("we are subtracting two numbers{a,b}")
    return (a-b)

sub = subtraction(15,8)
print(sub)

def division(a,b):
    print("we are dividing two numbers{a,b}")
    return (a//b)

divide = division(16,8)
print(divide)

def multiplication(a,b):
    print("we are multiplying two numbers{a,b}")
    return (a*b)

multiple = multiplication(9,9)
print(multiple)


#            Day 3: Age Checker
# Ask the user for their age.
# Tell them if they are:
# A child
# A teenager
# An adult
# Stretch
# Add a retirement message 

user = int(input("Enter your age: "))
if user < 13:
    print("you are a cute little baby")
elif user >= 13 and user <= 17:
    print('you are a teenager')
elif user >= 18 and user <= 55 :
    print('you are an adult')
elif user > 55:
    print("you should retire grandpa")
else:
    print('you wil be okay')


while True:
 
 def myAge(user):
    
  if user < 13:
    return("you are a cute little baby")
  elif user >= 13 and user <= 17:
    return('you are a teenager')
  elif user >= 18 and user <= 55 :
    return('you are an adult')
  elif user > 55:
    return("you should retire grandpa")
  else:
    print('you wil be okay')

 user = int(input("Enter your age: "))
 result = myAge(user)

 print(result)


#        Day 4: Even or Odd Checker
# Challenge
# Ask the user for a number.
# Check if the number is even or odd.
# Stretch
# Allow multiple checks until the user quits.

while True:
    number = int(input("enter a number: "))
    
    if number % 2 == 0:
        print(f'{number} is an even number')
    else :
        print (f'{number} is a odd number')
     
    proceed = input('Do you still want to continue (y/n)').lower()
    if proceed == 'n':
        quit()
    
while True:
  def checknumber(number):
    if number % 2 == 0:
        return(f'{number} is an even number')
    else :
        return (f'{number} is a odd number')
    
 number = int(input("enter a number: "))
 result = checknumber(number)
 print(result)

 proceed = input('Do you still want to continue (y/n)').lower()
 if proceed == 'n':
        quit()

#          Day 5: Number Guessing Game
# Challenge
# Generate a random number between 1 and 10.
# Let the user guess the number.
# Tell them if they are correct or wrong.
# Stretch
# Give hints (too high / too low).

import random

user = int(input('Enter a number from 1-10: '))
 guess = random.randint(1,10)

 if user < guess:
    print(f"the number you guess is too low,he number guessed is {guess}")
 elif user > guess:
    print(f"the number you guess is higher ,the number guessed is {guess}")
 elif user == guess:
    print("hurray,congratulation")
 else:
    print("thanks for playing")
 
 proceed = input('Do you wish to play again  (y/n)').lower()
 if proceed == 'n':
         quit()

import random

def guessNumber():

    user = int(input('Enter a number from 1-10: '))
    guess = random.randint(1,10)
    
    if user < guess:
      print(f"the number you guess is too low,the number guessed is {guess}")
    elif user > guess:
      print(f"the number you guess is higher ,the number guessed is {guess}")
    elif user == guess:
      print("hurray,congratulation")
    else:
      print("thanks for playing")
guessNumber()

# Day 6: Grade Calculator
# Challenge
# Ask for a student’s score.
# Assign a grade (A, B, C, D, F).
# Stretch
# Validate input (0–100 only).
while True:
 user = int(input("enter your score to check your grade:"))
 if user <= 49:
    print('you are a failure')
 elif user > 49 and user <= 60:
    print("grade d student you can do better")
 elif user > 60 and user <= 70:
    print("grade c student")
 elif user > 70 and user <= 80 :
    print("grade b student")
 elif user > 80 and user <= 100:
    print ("grade a student")
 else:
    print("enter only numbers from(1-100)")

 check = input("do you want to check again(y/n)").lower()
 if check == "n":
    quit()


def grade_checker():
    try:
        user = int(input("Enter your score to check your grade (0-100): "))
        
        if user < 0 or user > 100:
            print("Enter only numbers from 0 to 100")
        elif user <= 49:
            print('You are a failure')
        elif user <= 60:
            print("Grade D: You can do better")
        elif user <= 70:
            print("Grade C")
        elif user <= 80:
            print("Grade B")
        else:
            print("Grade A: Excellent!")
            
    except ValueError:
        print("Please enter a valid integer number.")

grade_checker()

#       Day 7: Simple Login System
# Challenge
# Store a correct username and password.
# Ask the user to log in.
# Grant or deny access.
# Stretch
# Limit login attempts to 3.
  
username = "adebimpe"
password = 202020

user_username = input("enter your username: ").lower()
user_password = int(input("enter your password: "))

if user_username == username and password == user_password:
    print("Successful login")
else:
    print("comeback when you know the correct input")

def login_system():
    correct_username = "adebimpe"
    correct_password = 202020  

    attempts = 3

    while attempts > 0:
        username = input("Enter username: ").lower()

        try:
            password = int(input("Enter password: "))
        except ValueError:
            print("Password must be numbers only")
            attempts -= 1
            continue

        if username == correct_username and password == correct_password:
            print("Login successful")
            return
        else:
            attempts -= 1
            print(f"Access denied. Attempts left: {attempts}")

    print("Account locked. Too many failed attempts.")

login_system()
