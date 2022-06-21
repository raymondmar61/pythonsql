import sqlite3

#Function Query The Database And Return All Records All Rows
def showall():
    #connecttotemporarydatabaseinmemory = sqlite3.connect(":memory:")
    connectdatabase = sqlite3.connect("customers.db") #if customer.db doesn't exist, sqlite3 creates customer.db file
    #Create a cursor.  A cursor tells the database what to do.  A cursor is a variable to execute SQL code?
    cursorc = connectdatabase.cursor()
    cursorc.execute("SELECT rowid, * FROM customers")
    forlooprowid = cursorc.fetchall()
    for eachforlooprowid in forlooprowid:
        print(eachforlooprowid)
        '''
        (1, 'John', 'Elder', 'john@codemy.com')
        (2, 'Tim', 'Smith', 'tim@codemy.com')
        (3, 'Mary', 'Brown', 'mary@codemy.com')
        (4, 'Wes', 'Brown', 'wes@brown.com')
        (5, 'Steph', 'Kuewa', 'steph@kuewa.com')
        '''
    connectdatabase.commit()
    connectdatabase.close()

#Function Search Database Where Clause Lookup
def lookupbyemail(emailaddress):
    connectdatabase = sqlite3.connect("customers.db")
    cursorc = connectdatabase.cursor()
    cursorc.execute("SELECT rowid, * FROM customers where email = (?)", (emailaddress,)) #YouTuber says a quirk.  The parenthesis and comma are required even if there's one variable(?)
    forlooprowid = cursorc.fetchall()
    for eachforlooprowid in forlooprowid:
        print(eachforlooprowid)
    connectdatabase.commit()
    connectdatabase.close()

#Function Add A New Record Or Add Data
def addone(first, last, email):
    connectdatabase = sqlite3.connect("customers.db")
    cursorc = connectdatabase.cursor()
    cursorc.execute("INSERT into customers values (?,?,?)", (first, last, email))
    connectdatabase.commit()
    connectdatabase.close()

#Function Add Multiple New Records Or Add Multiple Data
def addmultiples(recordslist):
    connectdatabase = sqlite3.connect("customers.db")
    cursorc = connectdatabase.cursor()
    cursorc.executemany("INSERT into customers values (?,?,?)", (recordslist))
    connectdatabase.commit()
    connectdatabase.close()


#Function Delete Record or Remove Data
def deleteusingrowid(id):
    connectdatabase = sqlite3.connect("customers.db")
    cursorc = connectdatabase.cursor()
    #cursorc.execute("delete from customers where rowid =", id) #sqlite3.OperationalError: incomplete input
    #cursorc.execute("delete from customers where rowid = (?)", id) #ValueError: parameters are of unsupported type
    cursorc.execute("DELETE from customers where rowid = (?)", str(id))
    connectdatabase.commit()
    connectdatabase.close()

#Function Delete Record or Remove Data
def deletebyemail(customeremail):
    connectdatabase = sqlite3.connect("customers.db")
    cursorc = connectdatabase.cursor()
    #cursorc.execute("delete from customers where email = (?)", customeremail) #sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 15 supplied.  customeremail is laura@smith.com and there are multiple rows with laura@smith.com email.
    #cursorc.executemany("DELETE from customers where email = (?)", (customeremail)) #Fail to delete by customeremail
    cursorc.execute("DELETE from customers where email = (?)", (customeremail,))
    connectdatabase.commit()
    connectdatabase.close()
