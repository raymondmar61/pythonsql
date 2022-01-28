import sqlite3
import csv
#Refresh basic Python csv open csv file
openfile = open("pythonbyexamplechallenges139145sqliteemployeestable.csv", "r")
for eachrow in openfile:
    print(eachrow)
    print(type(eachrow))
    '''
    1,Bob,Sales,25000

    <class 'str'>
    2,Sue,IT,28500

    <class 'str'>
    3,Tim,Sales,25000

    <class 'str'>
    4,Anne,Admin,18500

    <class 'str'>
    5,Paul,IT,28500

    <class 'str'>
    6,Simon,Sales,22000

    <class 'str'>
    7,Karen,Manufacturing,18500

    <class 'str'>
    8,Mark,Manufacturing,19000

    <class 'str'>
    9,George,Manufacturing,18500

    <class 'str'>
    10,Keith,Manufacturing,15000

    <class 'str'>
    '''
openfile.close()
openfiletolist = list(csv.reader(open("pythonbyexamplechallenges139145sqliteemployeestable.csv")))
employeeslist = []
for eachrow in openfiletolist:
    employeeslist.append(eachrow)
print(employeeslist) #print [['\ufeff1', 'Bob', 'Sales', '25000'], ['2', 'Sue', 'IT', '28500'], ['3', 'Tim', 'Sales', '25000'], ['4', 'Anne', 'Admin', '18500'], ['5', 'Paul', 'IT', '28500'], ['6', 'Simon', 'Sales', '22000'], ['7', 'Karen', 'Manufacturing', '18500'], ['8', 'Mark', 'Manufacturing', '19000'], ['9', 'George', 'Manufacturing', '18500'], ['10', 'Keith', 'Manufacturing', '15000']]
print(employeeslist[0]) #print ['\ufeff1', 'Bob', 'Sales', '25000']
print(employeeslist[0][1]) #print Bob

#Connect to the company database.  If the database doesn't exist, sqlite3 creates one.  The file is stored in the same folder as the program.
with sqlite3.connect("company.db") as db:
    cursor = db.cursor()
    cursor.execute("delete from employeestable") #Delete all rows for the purposes of starting over
    #Create table employeestable.  Four fields and their data type id, name, dept, salary.  name and dept can't be blank.
    cursor.execute("create table if not exists employeestable(id integer primary key, name text not null, dept text not null, salary integer);") #RM:  create table if not exists is an SQLite statement
    #Insert row in employeestable.  Single quotes for the text fields.  db.commit() saves changes.
    cursor.execute("insert into employeestable(id, name, dept, salary) values(1,'Bob','Sales',25000);")
    db.commit()
    #Enter new data with variables
    newid = 2
    newname = "Sue"
    newdept = "IT"
    newsalary = 28500
    cursor.execute("insert into employeestable(id, name, dept, salary) values(?,?,?,?)", (newid, newname, newdept, newsalary))
    db.commit()
    #Display all the data from employeestable
    cursor.execute("select * from employeestable;")
    print(cursor.fetchall()) #print [(1, 'Bob', 'Sales', 25000), (2, 'Sue', 'IT', 28500)]
#Must be the last line to close the database
db.close()

#Use csv module to enter data to employeestable
import csv
with sqlite3.connect("company.db") as db:
    cursor = db.cursor()
    cursor.execute("delete from employeestable")
    openfiletolist = list(csv.reader(open("pythonbyexamplechallenges139145sqliteemployeestable.csv", encoding='utf-8-sig'))) #The encoding removes the \ufeff
    employeeslistcomprehension = [eachrow for eachrow in openfiletolist]
    print(employeeslistcomprehension) #print [['\ufeff1', 'Bob', 'Sales', '25000'], ['2', 'Sue', 'IT', '28500'], ['3', 'Tim', 'Sales', '25000'], ['4', 'Anne', 'Admin', '18500'], ['5', 'Paul', 'IT', '28500'], ['6', 'Simon', 'Sales', '22000'], ['7', 'Karen', 'Manufacturing', '18500'], ['8', 'Mark', 'Manufacturing', '19000'], ['9', 'George', 'Manufacturing', '18500'], ['10', 'Keith', 'Manufacturing', '15000']]
    for eachemployeeslistcomprehension in employeeslistcomprehension:
        addid = int(eachemployeeslistcomprehension[0])
        addname = eachemployeeslistcomprehension[1]
        adddept = eachemployeeslistcomprehension[2]
        addsalary = int(eachemployeeslistcomprehension[3])
        cursor.execute("insert into employeestable(id, name, dept, salary) values(?,?,?,?)", (addid, addname, adddept, addsalary))
        db.commit()
    cursor.execute("select * from employeestable;")
    print(cursor.fetchall()) #print [(1, 'Bob', 'Sales', 25000), (2, 'Sue', 'IT', 28500), (3, 'Tim', 'Sales', 25000), (4, 'Anne', 'Admin', 18500), (5, 'Paul', 'IT', 28500), (6, 'Simon', 'Sales', 22000), (7, 'Karen', 'Manufacturing', 18500), (8, 'Mark', 'Manufacturing', 19000), (9, 'George', 'Manufacturing', 18500), (10, 'Keith', 'Manufacturing', 15000)]
db.close()
