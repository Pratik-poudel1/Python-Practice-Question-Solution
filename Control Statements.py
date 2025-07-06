# #===================== PRACTICE QUESTIONS ===========================


# # WAP to Print the multiplication table of a number using a for loop.
# num=int(input('Enter a number: '))
# for i in range(1,11):
#     print(f'{num} * {i} = {num*i}')


# # WAP to Print the first 10 Fibonacci numbers using a while loop.
# a=1
# b=1
# for i in range (1,11):
#     c=a+b
#     print (a,end=" ")
#     a=b
#     b=c


# # WAP to Use a loop to find factorial of a number. 
# num=int(input('Enter any number: '))
# factorial=[]
# while True:
#     for i in range (1,num+1):
#         if num%i==0 :
#            factorial.append(i)
#     break
# print(f'Factorial of {num} : {factorial}') 


# # WAP to Use nested loops to print a pyramid pattern of stars.
# rows=int(input('Enter the no. of rows of pyramid: '))
# for i in range(1,rows+1):
#     for j in range(1,rows-i+1):
#         print(' ',end=' ')
#     for k in range(1,2*i):
#         print('*',end=' ')
#     print()


# # WAP to that breaks when the number 5 is entered. 
# while True:
#     num=int(input('Enter a number: '))
#     if num==5:
#         print('Number 5 was entered')
#         break
#     else:
#         print('You entered: ',num)


# # WAP to Continue printing numbers from 1 to 10 but skip multiples of 3. 
# for i in range(1,11):
#     if i%3 !=0:
#         print(i,end=' ')


# # WAP to  Print all prime numbers between 1 and 50.
# prime=[] 
# for i in range(1,51):
#     count=0
#     for a in range (1,i+1):
#         if i%a==0:
#             count +=1
#     if count==2:
#         prime.append(i)
# print('List of Prime Numbers: ',prime)

# # WAP to  Use if-elif-else to implement a grading system. 
# percentage=int(input('Enter your Percentage: '))
# if percentage>=90:
#     grade='A+'
# elif percentage>=80:
#     grade='A'
# elif percentage>=70:
#     grade='B+'
# elif percentage>=60:
#     grade='B'
# elif percentage>=50:
#     grade='C+'
# elif percentage>=40:
#     grade='C'
# else:
#     grade='Fail'
# print('Your Grade: ',grade)


# # WAP to Simulate a simple login system with 3 login attempts. 
# attempts=0
# max_attempts=3
# logged_in=False
# users=[
#     {'username':'pratik poudel','password':'pratik002'},
# ]
# while attempts<max_attempts:
#     user_name=input('Enter your username: ')
#     password=input('Enter your password: ')
#     for user in users:
#         if user['username']==user_name and user['password']==password:
#             print(f'Welcome ! {user_name}')
#             logged_in=True
#             break
#         if logged_in:
#             break
#     else:
#         print('Username or Password is not correct')
#         attempts+=1

# if not logged_in:
#     print('Too many Failed attempts.Exiting....')
#     exit()


# # WAP to Create a number guessing game using a loop and conditions. 
# print('##################### Welcome Our Game ##########################')
# print('\n\nYou have to guess numbers and in some numbers there are hidden gifts.')
# import random

# # Generate a random number between 1 and 10
# secret_number = random.randint(1, 10)
# while True:
#     guess = int(input("Guess a number between 1 and 10: "))
#     if guess == secret_number:
#         print("🎉 Correct! You guessed the number.")
#         break
#     elif guess < secret_number:
#         print("Too low. Try again.")
#     else:
#         print("Too high. Try again.")


# #  Write a recursive function to calculate factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# num = int(input("Enter a number to find its factorial: "))
# print("Factorial of", num, "is", factorial(num))


# #  Create a function to count vowels in a string.
# def count_vowels():
#     count = 0
#     vowels = "AEIOUaeiou"
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count
# string = input("Enter a string: ")
# print("Number of vowels:", count_vowels())


# # Write a function to calculate the GCD of two numbers. 
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# print("Calculate GCD of two numbers")
# num1 = int(input('Enter a Number: '))
# num2 = int(input('Enter a Number: '))
# print(f"The GCD of {num1} and {num2} is: ",gcd(num1, num2))


# # Create a function that returns True if a string is a valid email. 
# def email_verify():
#     if '@' in email and '.' in email :
#         return True
#     else:
#         return False
# email=input('Enter Email You want to create: ')
# print(email_verify())


# #  Create a lambda function to square a number. 
# square=lambda x:x**2
# num =int(input('Enter a Number: '))
# print(f'The Square of {num} is',square(num))


# #  Use *args and **kwargs in a function to demonstrate flexibility.
# def flexible_function(*args, **kwargs):
#     print("Positional arguments (args):", args)
#     print("Keyword arguments (kwargs):", kwargs)
# flexible_function(69, 2, 4, name="Pratik Poudel", age=18, country="Nepal")

