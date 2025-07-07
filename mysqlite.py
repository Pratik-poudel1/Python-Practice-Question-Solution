# #===================== PRACTICE QUESTIONS ===========================


# #  Connect to a MySQL database and create a table for storing employee records.
import sqlite3

conn=sqlite3.connect('Practice Question/Mysqlite/employeeinfo.sqlite3')
cursor=conn.cursor()
def create_employeeinfo_table():
    sql = '''
    CREATE TABLE IF NOT EXISTS employeeinfo (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_name TEXT NOT NULL,
        employee_email TEXT NOT NULL,
        address TEXT NOT NULL,
        phone_no INTEGER NOT NULL
    )
    '''
    cursor.execute(sql)
    conn.commit()
    print('Employee Info table created successfully')
create_employeeinfo_table()




# Write a program to insert, update, delete, and fetch employee records from the database.

def insert_info(employee_name,employee_email,address, phone_no):
    sql = '''
    INSERT INTO results (employee_name,employee_email,address, phone_no)
    VALUES (?, ?, ?, ?)
    '''
    cursor.execute(sql, (employee_name,employee_email,address, phone_no))
    conn.commit()
    print("Information inserted successfully!")

employee_name=input("Enter Employee's Name: ")
employee_email=input("Enter Employee's Email: ")
address=input("Enter Employee's Address: ")
phone_no=input("Enter Employee Phone No.: ")

insert_info(employee_name,employee_email,address, phone_no)



print('What action do you want to preform in the Table: ')
print('1. Insert')
print('2. Update')
print('3. Delete')
print('4. Fetch')

opt=input('Enter your Choice (1/2/3/4): ')
if opt=='1':
    insert_info()
elif opt=='2':
    def update(employee_id,employee_name,employee_email,address, phone_no,):
        sql='UPDATE employeeinfo set employee_name=?,employee_email=?,address=?, phone_no=? WHERE employee_id=?'
        cursor.execute(sql,(employee_name,employee_email,address, phone_no,employee_id))
        conn.commit()
        print('Data Updated Sucessfully')
    update(2,'Pratik Poudel','pratikpoudel@gmail.com','ktm',9762790450)
elif opt=='3':
    del_=input('Enter the no. of row you want to DELete:')
    def delete(id):
        sql='DELETE FROM results WHERE employee_id=?'
        cursor.execute(sql,(id,))
        conn.commit()
        print('Data deleted Sucessfully.')
    delete(del_)
elif opt=='4':
    def show(employee_id):
        sql = 'SELECT * FROM employeeinfo WHERE employee_id_id = ?'
        cursor.execute(sql, (employee_id,))
        result = cursor.fetchone()

        if result:
            print('Employee Id\t Employee Name\t\t Employee Email\t\t\t Address\t Phone no.\t ')
            print(f'{result[0]}\t   \t{result[1]}\t\t{result[2]}\t\t\t{result[3]}\t')
        else:
            print("No record found for this Employee ID.")
    employee_id = int(input("Enter Employee ID to view info: "))
    show(employee_id)
else:
    print('Invalid Option!!!!!!!!')
    print('Exiting')
    exit()