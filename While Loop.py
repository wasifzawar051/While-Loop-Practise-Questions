# QUESTION-1 Write a program that uses a while loop to count from 1 to 10 and print each number.
n = 0
while n <= 10:
    print(n)
    n += 1
    
# Question-2 Create a while loop to print all even numbers from 1 to 20.
n = 0
while n <= 20:
    print(n)
    n += 2
    
#QUESTION-3 Write a program using a while loop to calculate the sum of the first 10 natural numbers.
n = 0
SUM = 0
while n <= 10:
    SUM += n
    n += 1
print(f"The sum of first 10 natural numbrs is {SUM}")

#QUESTION-4 Write a program that prompts the user to enter numbers. The loop should keep asking for numbers
#until the user enters a negative number. When the loop exits, print the total sum of the numbers entered (excluding the negative number).
Total_sum = 0
while True:
    number=float(input("Enter your numbe(and negative number if you want to exit):"))
    if number < 0:
        break
    Total_sum += number
print(f"The SUM of the numbers entered is {Total_sum}") 

#QUESTION-5 Create a guessing game where the user has to guess a number between 1 and 100.
# Use a while loop to allow the user to keep guessing until they get it right. Provide hints if the guess is too high or too low.
import random
secret_number = random.randint(1,100)
print("Welcome to the Guessing Game!\nMake a guess and enter your number")
while True:
    Guess = int(input("Enter your GUESSED number(Enetr 0 if you wnat to give up):"))
    if Guess > 0: 
        if Guess < secret_number:
            print("To low value!\nTry again")
        elif Guess > secret_number:
            print("To high value!\nTry again")
        else:
            print("Congratulations! You have Guessed correctly.")
    else:
        print(f"The SECERET NUMBER was {secret_number}.")
        break
      
# QUESTION-6 Write a program to calculate the factorial of a given positive integer using a while loop.
num=int(input("Enter your number:"))
if num < 0 :
    print("Factorail for negative number is not defined.")
elif num == 0 :
    print("The FACTORIAL of 0 is 1.")
else:
    Factorial = 1
    i = num
    while i > 0:
        Factorial *= i
        i -= 1
    print(f"The FACTORIAL of the {num} is {Factorial}.")
    
# QUESTION-7 Write a program that uses a while loop to take in a series of numbers from the user.
# The loop should stop when the user enters "done". Calculate and print the average of the entered numbers.
print("\nAverage Calculator")
total_sum = 0
count = 0
print("Enter numbers to calculate the average. Type 'done' when finished.")
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")
    if user_input.lower() == "done":
        break
    try:
        number = float(user_input)
        total_sum += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a number.")
if count > 0:
    average = total_sum / count
    print("The average of the entered numbers is:", average)
else:
    print("No numbers were entered.")

   # QUESTION-8 Print the Fibonacci sequence up to a specified number n (where n is an integer input by the user).
print("\n Fibonacci Sequence")
n = int(input("Enter a positive integer to print the Fibonacci sequence up to: "))
a, b = 0, 1
print("Fibonacci sequence up to", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b 
print()       
        