# #===================== PRACTICE QUESTIONS ===========================

# # Write a program to read a text file and print its content.
# file=open('Practice Question/File Handling/data.txt','r')
# content=file.read()
# print(content)
# file.close()


# # Write a program to count the number of lines, words, and characters in a file.
# file=open('Practice Question/File Handling/data.txt','r')
# lines = file.readlines()
# line_count = len(lines)
# for line in lines:
#     word_count = sum(len(line.split()))
# for line in lines:
#     char_count = sum(len(line))
# print(f"Lines: {line_count}")
# print(f"Words: {word_count}")
# print(f"Characters: {char_count}")
# file.close()


# # Write a program to copy content from one file to another.
# file=open('Practice Question/File Handling/data.txt','r')
# content=file.read()
# file1=open('Practice Question/File Handling/copydata.txt','x')
# file1.write(content)
# file.close()
# file1.close()


# # Append a line of text to an existing file. 
# file=open('Practice Question/File Handling/data.txt','a')
# file.write('\nThis is the new line i added')
# file.close()


# #  Write user input to a file and then read it.
# file=open('Practice Question/File Handling/data.txt','a')
# line=input('Enter a line You want to add: ')
# file.write('\n',line)
# file.close()


# # Store student records in a file and retrieve them.
# file=open('Practice Question/File Handling/student.txt','a')
# name=input('Enter Student Name: ')
# roll_no=input('Enter Student Roll no: ')
# address=input('Enter Student Address: ')
# phone_no=input('Enter Student Phone Number: ')
# file.write(f'Student Name: {name}\n')
# file.write(f'Roll no: {roll_no}\n')
# file.write(f'Address: {address}\n')
# file.write(f'Phone No: {phone_no}\n')
# file.close()
# file=open('Practice Question/File Handling/student.txt','r')
# print(file.read())
# file.close()


# # Create a simple log system that writes time-stamped logs to a file.
# import datetime
# current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# file=open('Practice Question/File Handling/data.txt','a')
# file.write(f"\n{current_time} \n")
# if __name__ == "__main__":
#     print("Program started")
#     print("Something important happened")


# # Write a function to search for a word in a file and return its line number(s). 
# def search_word(file):
#     line_numbers = []
#     file =open('Practice Question/File Handling/student.txt', 'r')
#     for i, line in enumerate(file, start=1):
#         if word in line:
#             line_numbers.append(i)
#     return line_numbers
# word = input("Enter word to search: ")
# result = search_word('Practice Question/File Handling/student.txt')
# if result:
#     print(f"'{word}' found on line(s): {result}")
# else:
#     print(f"'{word}' not found in the file.")


# # Read a CSV file and print its content.
# import csv
# with open('Practice Question/File Handling/data.csv', mode='r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# # Save a dictionary as JSON and read it back using the json module.
# import json
# data = {
#     "name": "Pratik",
#     "age": 17,
#     "city": "Kathmandu",
#     "skills": ["Python", "HTML", "CSS"]
# }
# with open('Practice Question/File Handling/data.json', 'w') as file:
#     json.dump(data, file, indent=4)
# with open('Practice Question/File Handling/data.json', 'r') as file:
#     loaded_data = json.load(file)
# print(loaded_data)


