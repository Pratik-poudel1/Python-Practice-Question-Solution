# #===================== PRACTICE QUESTIONS ===========================


# # WAP to Take user input for name and age and display a greeting. 
# name=input('Enter your name: ')
# age=input('Enter your age: ')
# print(f'My name is {name}.I am {age} years old.')


# #Ask the user to enter 3 numbers and print their sum. 
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# c=int(input('Enter third number: '))
# sum=a+b+c
# print(f'Sum of the three numbers: {sum}')


# #Create a CLI calculator that takes two numbers and
# #  an operator as input and prints the result. 
# while True:
#     a=int(input('Enter first number: '))
#     opt=input('Enter any operator(+,-,*,/,%): ')
#     b=int(input('Enter second number: '))
#     if opt=='+':
#         result=a+b
#         print('Result: ',result)
#         break
#     elif opt=='%':
#         result=a%b
#         print('Result: ',result)
#         break
#     elif opt=='-':
#         result=a-b
#         print('Result: ',result)
#         break
#     elif opt=='*':
#         result=a*b
#         print('Result: ',result)
#         break
#     elif opt=='/':
#         if b!=0:
#             result=a/b
#             print('Result: ',result)
#             break
#     else:
#         print('Invalid Operator')
#         again=input('Do you want to try again (Y/N) ?')
#         if again.lower()=='y':
#             print('Reloding.....')
#             print('\n\n')
#         elif again.lower()=='n':
#             print('Press enter to exit')
#             exit()
#             break
#         else:
#             print('If you donot understand english.\nWhy are you even using computer.\n\t\tCAVEMAN!!!!!!')


# # WAP to Ask the user to input a sentence and count the number of words.
# sen=input('Enter a sentence: ')
# words=sen.split()
# word_count=len(words)
# print('Number of words in the sentence: ',word_count)


# # WAP to Take an integer and print its binary, octal, and hexadecimal representation.
# num=int(input('Enter an integer: '))
# print('Binary number: ',bin(num)) 
# print('Octal humber: ',oct(num)) 
# print('Hexadecimal number: ',hex(num)) 
