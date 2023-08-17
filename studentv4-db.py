import csv 
import sqlite3
from pathlib import Path

file_name = 'students.sqlite'
conn = sqlite3.connect(file_name)
c = conn.cursor()

students = []
class Student:   
    def __init__(self,name,classs,section,roll_no):
        self.name = name
        self.classs = classs
        self.section = section
        self.roll_no = roll_no
    
    def __str__(self):
        ret = 'Name=' + self.name + ', class=' + self.classs + ', Section=' + self.section + ', Roll number=' + self.roll_no
        return ret
    
    def __repr__(self):
        ret = self.name + ',' + self.classs + ',' + self.section + ',' + self.roll_no
        return ret
    
    def record(self):
        rec = [self.name, self.classs,self.section, self.roll_no]
        return rec
    
    @classmethod
    def header(cls):
        rec = ['Name', 'Class', 'Section', 'Roll Number']
        return rec

###########################################
def add_students_to_list():
    name = input(' Enter Name: ')
    classs = input(' Enter classs: ')
    section = input(' Enter section: ')
    roll_num = input(' Enter Roll number: ')
    students.append(Student(name, classs, section, roll_num))

        
############################################
def print_students_from_list():
    print('\nNumber of students in the list =', len(students))
    if len(students) > 0:
        print('------------------------------------------------------------------------------')
        for student in students:
            print(repr(student))  
        print('------------------------------------------------------------------------------')
        
#############################################
def save_students_to_txt_file():
    with open('students-v3.txt','a', encoding='utf-8') as file:
        file.write('\n') 
        for student in students:
            file.write(repr(student) + '\n')  
        print("Details Saved!...")        

##########################################

def load_students_from_txt_file():
    with open('students-v3.txt','r', encoding='utf-8') as file: 
        count = 0
        row = []
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            l = line.split(',')
            if len(l) != 4:
                continue
            students.append(Student(l[0], l[1], l[2], l[3]))
            count += 1
        print('Loaded ', count, ' students from students-v3.txt')
    
##########################################

def save_students_to_csv_file():
    with open('GFG2.csv','a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerow(Student.header())
        for student in students:
            write.writerow(student.record())
        print("Details Saved!..............")  


##########################################

def load_students_from_csv_file():
    with open('GFG2.csv','r', encoding='utf-8') as f:
        count = 0
        row = []
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            if len(row)!=4:
                continue
            students.append(Student(row[0], row[1], row[2], row[3]))
            #students.append(student)
            count += 1
        print('Loaded ', count, ' students from GFG2.csv')

##########################################

def isStudentsTableExists():
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='students' ''')
    return c.fetchone()[0]==1

def prepare_database():
    # db_file = Path(file_name)   # only to test if the database file is already present
    if not isStudentsTableExists():
        # database file not present, so create database and also create relevant tables once
        c.execute('CREATE TABLE students (name text, classs text, section text, rollno real)')

def save_students_to_db_file():
    prepare_database()
    for student in students:
        print(student)
        c.execute('INSERT INTO students VALUES (?, ?, ?, ?)', (student.name, student.classs, student.section, student.roll_no))
    conn.commit()

def load_students_from_db_file():
    prepare_database()
    count = 0
    c.execute('SELECT * FROM STUDENTS')  
    rows = c.fetchall() 
    for row in rows:
        student = Student(row[0], row[1], row[2], row[3])
        students.append(student)
        count +=1
    print('Loaded',count,'students from students.sqlite')    
##########################################
def exit_app():
    c.close()
    conn.close()
    quit()
    
##########################################
while True:
    print('\n1 --> Add student')
    print('2 --> print students')
    print('3 --> Save students to txt')
    print('4 --> load students from txt')
    print('5 --> Save students to csv')
    print('6 --> load students from csv')
    print('7 --> Save students to database')
    print('8 --> load students from database')
    print('9 --> exit')

    choice = input(' Select your choice: ')
    if len(choice)==0: choice=99

    if int(choice) == 1:
        add_students_to_list()
    elif int(choice) == 2:
        print_students_from_list()
    elif int(choice) == 3:
        save_students_to_txt_file()
    elif int(choice) == 4:
        load_students_from_txt_file()
    elif int(choice) == 5:
        save_students_to_csv_file()
    elif int(choice) == 6:
        load_students_from_csv_file()
    elif int(choice) == 7:
        save_students_to_db_file()
    elif int(choice) == 8:
        load_students_from_db_file()
    elif int(choice) == 9:
        exit_app()
    else:
        confirmation = input('Are you sure! you want to quit? (y/n)')
        if confirmation == 'y':
            exit_app()
        elif confirmation == 'n':
            continue

##########################################