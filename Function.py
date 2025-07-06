# #===================== PRACTICE QUESTIONS ===========================


# # Write a function to check if a number is a palindrome. 
# def palindrome(num):
#     orginal =str(num)
#     reversed_num=orginal[::-1]
#     if orginal==reversed_num:
#         return True
#     else:
#         return False
    
# num=int(input('Enter a Number: '))
# if palindrome(num):
#     print('Palindrome Number')
# else:
#     print('Not a Palindrome Number')


# # Write a function to reverse a string. 
# def reve(word):
#     orginal=word
#     reversed_str=orginal[::-1]
#     return reversed_str
# word=input('Enter any String: ')
# print('Reversed String: ',reve(word))


# # Create a calculator using functions for add, subtract, multiply, and divide. 
# def addition(a,b):
#     return a+b
# def subtraction(a,b):
#     return a-b
# def multiplication(a,b):
#     return a*b
# def division(a,b):
#     if b!=0:
#         return a/b
#     else:
#         return 'Error! Division by Zero'
# a=int(input('Enter First Number: '))
# opt=input('Enter an Operator(+,-,*,/): ')
# b=int(input('Enter Second Number: '))
# if opt=='+':
#     print('Addition:',addition(a,b))
# elif opt=='-':
#     print('Subtraction:',subtraction(a,b))
# elif opt=='*':
#     print('Multiplication:',multiplication(a,b))
# elif opt=='/':
#     print('Division:',division(a,b))
# else:
#     print('Invalid Operator')


# #  Write a function that takes a list and returns the max and min.
# def find_max_min(numbers):
#     maximum = max(numbers)
#     minimum = min(numbers)
#     print("The Biggest Number in The List:", maximum)
#     print("The Smallest Number in The List:", minimum)

# user_list = []
# num = int(input("Enter the number of elements you want to enter in the list: "))

# for i in range(num):
#     number = int(input("Enter Number: "))
#     user_list.append(number)

# find_max_min(user_list)
