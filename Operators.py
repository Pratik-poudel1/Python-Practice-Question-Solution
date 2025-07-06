# #===================== PRACTICE QUESTIONS ===========================


# #Write a program to check if a number is even or odd using the modulo operator. 
# num=int(input('Enter a number: '))
# if num%2==0:
#     print(f'{num} is an even number.')
# else:
#     print(f'{num} is a odd number.')


# # WAP to Take a number and raise it to a power using **. 
# num=int(input('Enter a number: '))
# power=int(input('Enter by how much power do you want to raise the num: '))
# num **= power
# print('Result: ',num)


# # WAP to Use logical operators to check if a number is between 10 and 100. 
# num=int(input('Enter a number: '))
# if num>10 and num<100:
#     print(f'{num} is in between 10 and 100.')
# else:
#     print(f'{num} isnot in between 10 and 100.')


# # WAP to Demonstrate the difference between is and ==. 
# # Using two variables with the same value
# a = [1, 2, 3]
# b = [1, 2, 3]# == checks if values are equal
# print("a == b:", a == b)  # True because values are the same is checks if both refer to the same object in memory
# print("a is b:", a is b)  # False because they are different objects Assigning same reference
# c = a
# print("a == c:", a == c)  # True
# print("a is c:", a is c)  # True because c points to the same object as a


# # WAP to Take three numbers and print the largest using conditional and comparison operators.
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# c=int(input('Enter third number: '))
# if a>b and a>c:
#     largest=a
# elif b>c and b>a:
#     largest=b
# else: 
#     largest=c
# print('Largest number: ',largest)