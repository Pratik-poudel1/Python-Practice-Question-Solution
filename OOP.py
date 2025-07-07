# #===================== PRACTICE QUESTIONS ===========================


# # Create a class Car with attributes and methods to start and stop. 
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.is_running = False 

#     def start(self):
#         if not self.is_running:
#             self.is_running = True
#             print(f"{self.brand} {self.model} has started.")
#         else:
#             print(f"{self.brand} {self.model} is already running.")

#     def stop(self):
#         if self.is_running:
#             self.is_running = False
#             print(f"{self.brand} {self.model} has stopped.")
#         else:
#             print(f"{self.brand} {self.model} is already stopped.")

# brand=input('Enter the brand of car you are driving: ')
# model=input('Enter the model of car you are driving: ')
# my_car = Car(brand,model)
# my_car.start()
# my_car.stop()


# # Create a BankAccount class with deposit and withdraw methods.
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'₹{amount} has been deposited. Current balance: ₹{self.balance}')

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f'Insufficient funds! Current balance: ₹{self.balance}')
#         else:
#             self.balance -= amount
#             print(f'₹{amount} has been withdrawn. Current balance: ₹{self.balance}')
# account = BankAccount()
# print('Welcome to our Bank')

# while True:
#     print('\n1. Deposit')
#     print('2. Withdraw')
#     print('3. Exit')

#     opt = input('\nEnter your Choice (1/2/3): ')
#     if opt == '1':
#         amt = int(input('Enter the amount you want to Deposit: '))
#         account.deposit(amt)
#     elif opt == '2':
#         amt = int(input('Enter the amount you want to Withdraw: '))
#         account.withdraw(amt)
#         break
#     elif opt == '3':
#         print('Thank you for using our service. Goodbye!')
#         break
#     else:
#         print('Invalid Option! Please try again.')


# # Implement inheritance: Animal → Dog, Cat. 
# class animal:
#     def call(self):
#         print('Your are an animal.')

# class dog(animal):
#     def speak(self):
#         print('Dog barks')

# class cat(animal):
#     def speak(self):
#         print('Cat meows')

# dog_obj=dog()
# cat_obj=cat()

# dog_obj.call()
# dog_obj.speak()
# cat_obj.call()
# cat_obj.speak()


# #  Demonstrate method overriding in a subclass.
# class Animal:
#     def speak(self):
#         print("The animal makes a sound.")

# class Dog(Animal):
#     def speak(self): 
#         print("The dog barks.")

# class Cat(Animal):
#     def speak(self):  
#         print("The cat meows.")

# a = Animal()
# a.speak()

# d = Dog()
# d.speak() 

# c = Cat()
# c.speak() 


# #  Use @staticmethod and @classmethod in a class
# class Student:
#     school_name = "Global High School"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def get_school_name(cls):
#         return cls.school_name
#     @staticmethod
#     def is_teenager(age):
#         return 13 <= age <= 19

# s1 = Student("Alice", 15)

# print("Student Name:", s1.name)
# print("School Name:", Student.get_school_name())     
# print("Is Teenager:", Student.is_teenager(s1.age))   


# #  Write a class to model a student with name, age, and marks. Add a method to calculate grade. 
# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks 
#     def calculate_grade(self):
#         if self.marks >= 90:
#             return 'A+'
#         elif self.marks >= 80:
#             return 'A'
#         elif self.marks >= 70:
#             return 'B+'
#         elif self.marks >= 60:
#             return 'B'
#         elif self.marks >= 50:
#             return 'C'
#         elif self.marks >= 40:
#             return 'D'
#         else:
#             return 'F'
# student1 = Student("Sita", 16, 85)
# print("Name:", student1.name)
# print("Age:", student1.age)
# print("Marks:", student1.marks)
# print("Grade:", student1.calculate_grade())


# # Create a Library class to manage books (add, remove, list).
# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book_name):
#         self.books.append(book_name)
#         print(f'"{book_name}" has been added to the library.')

#     def remove_book(self, book_name):
#         if book_name in self.books:
#             self.books.remove(book_name)
#             print(f'"{book_name}" has been removed from the library.')
#         else:
#             print(f'"{book_name}" not found in the library.')

#     def list_books(self):
#         if not self.books:
#             print("The library has no books.")
#         else:
#             print("Books available in the library:")
#             for book in self.books:
#                 print(f"- {book}")

# lib = Library()
# lib.add_book("The Alchemist")
# lib.add_book("Harry Potter")
# lib.list_books()
# lib.remove_book("The Alchemist")
# lib.list_books()


# # Overload the + operator for a custom class.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# p1 = Point(2, 3)
# p2 = Point(4, 5)
# p3 = p1 + p2  
# print("Point 1:", p1)
# print("Point 2:", p2)
# print("Sum:", p3)


# #  Use private and protected variables in a class and access them with methods. 
# class Student:
#     def __init__(self, name, age, grade):
#         self._name = name        
#         self.__age = age         
#         self.__grade = grade     

#     def get_details(self):
#         return f"Name: {self._name}, Age: {self.__age}, Grade: {self.__grade}"

#     def set_age(self, new_age):
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             print("Invalid age.")

#     def get_age(self):
#         return self.__age

# s1 = Student("Ram", 16, "A")
# print(s1.get_details())

# s1.set_age(17)
# print("Updated Age:", s1.get_age())


# # Create a class that keeps track of how many objects are created (use class variables).
# class Counter:
#     object_count = 0

#     def __init__(self):
#         Counter.object_count += 1
#         print(f"Object {Counter.object_count} created.")

#     @classmethod
#     def total_objects(cls):
#         return cls.object_count

# a = Counter()
# b = Counter()
# c = Counter()
# print("Total objects created:", Counter.total_objects())
