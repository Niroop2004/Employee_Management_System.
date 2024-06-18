import pymysql
from tkinter import messagebox

def connect_database():
    """Connects to the MySQL database and creates the 'employee_data' database and 'data' table if they dont exist."""
    global mycursor,conn
    try:
        #In order to connect Python script to Mysql database we use Connection object using connection class in pymysql
        conn = pymysql.connect(host='localhost', user='root', password='1234')
        #In order to run the query we have to use cursor object that we can create using conn object which will call the cursor class.  
        mycursor = conn.cursor()
        # Create database, and using this mycursor object we can execute the queries
        mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
        # Use the created database
        mycursor.execute('USE employee_data')
        # Create table
        mycursor.execute('''CREATE TABLE IF NOT EXISTS data (
            Id VARCHAR(30) PRIMARY KEY,
            Name VARCHAR(30) NOT NULL,
            Phone VARCHAR(15),
            Role VARCHAR(20),
            Gender VARCHAR(20),
            Salary DECIMAL(10,2)
        )''')
        conn.commit()  # Commit changes to the database
        messagebox.showinfo('Success', 'Database and table created successfully!')

    except pymysql.Error as err:
        messagebox.showerror('Error','Error connecting to database')

#once check what is the sgnificnce of commit()
def insert(id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    conn.commit()

# once check what will fetchone do ?
def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE Id=%s',id)
    result = mycursor.fetchone()
    return result[0]>0


def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result


def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()


def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    conn.commit()

def search(option, value):
  mycursor.execute(f'SELECT * FROM data WHERE {option}=%s', value)
  # Change 'Employee_Id' to the actual column name (e.g., EmpID)
  result = mycursor.fetchall()
  return result
  
def delete_all_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()

# Connect to the database and create tables only on first run
connect_database()

