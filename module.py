# #===================== PRACTICE QUESTIONS ===========================


# # Create a module with arithmetic functions and import it into another file. 
# import arithmetic
# num1=int(input('Enter a Number: '))
# opt=input('Enter an Operator (+,-,*,/): ')
# num2=int(input('Enter a Number: '))
# if opt=='+':
#     arithmetic.add(num1,num2)
# elif opt=='-':
#     arithmetic.add(num1,num2)
# elif opt=='*':
#     arithmetic.add(num1,num2)
# elif opt=='/':
#     arithmetic.add(num1,num2)
# else:
#     print('Invalid Option...')
#     again = input('Do you want to try again? (Y/N): ')
#     if again.lower() != 'y':
#         print('Exiting')
#         exit()


# # Use the math module to calculate the square root, sin, and log of a number.
# import math
# num=int(input('Enter a Number To Find the square of it: '))
# ang=int(input('Enter Angle to find sin value of it: '))
# base=int(input('Enter a num to find log of it: '))
# print(f'The Square of {num} is',math.sqrt(num))
# print(f'The sin value of {ang} is',math.sin(math.radians(ang)))
# print(f'The Log of {base} is',math.log(base))


# #  Use the random module to simulate dice rolls. 
# import random
# roll = input('Do you want to Roll a Dice ? (Y/N): ')
# if roll.lower() != 'y':
#     print('Exiting')
#     exit()
# print('Dice Rolled.')
# print('You got',random.randint(1,6))


# #  Use the datetime module to calculate days between two dates.
# from datetime import datetime
# print('Enter the dates in YYYY-MM-DD format...')
# date1 = input('Enter First Date: ')
# date2 = input('Enter Second Date: ')
# d1 = datetime.strptime(date1, '%Y-%m-%d')
# d2 = datetime.strptime(date2, '%Y-%m-%d')
# diff = d1 - d2
# print('Days:', abs(diff.days))


# # Write a module that generates a list of random passwords. 
# import string
# import random
# def create_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ""
#     for i in range(length):
#         password += random.choice(characters)
#     return password
# def create_password_list(count, length):
#     passwords = []
#     for i in range(count):
#         passwords.append(create_password(length))
#     return passwords
# if __name__ == "__main__":
#     how_many = int(input("How many passwords do you want? "))
#     how_long = int(input("How long should each password be? "))

#     result = create_password_list(how_many, how_long)

#     print("\nGenerated Passwords:")
#     for i, pwd in enumerate(result, 1):
#         print(f"{i}. {pwd}")


# # Create a reusable utility module with string, math, and list functions.
# import utility
# print(utility.count_vowels("Hello World"))  
# print(utility.add(5, 7))                    
# print(utility.find_max([10, 20, 5, 8]))     
# print(utility.is_palindrome("madam"))       


# # Use the os module to list all files in a directory. 
# import os
# folder = input("Enter folder path: ")
# items = os.listdir(folder)
# print("\nItems in the folder:")
# for name in items:
#     print(name)


# # Use the sys module to accept command-line arguments and print them.
# import sys
# print("Command-line arguments:")
# for arg in sys.argv:
#     print(arg)

