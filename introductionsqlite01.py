import sqlite3
class Employee:
    """A sample Employee class"""

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
    @property
    def email(self):
        return "{}.{}@email.com".format(self.firstname, self.lastname)
    @property
    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.firstname, self.lastname, self.pay)


employee001 = Employee("John", "Doe", 80000)
employee002 = Employee("Jane", "Doe", 90000)
print(employee001.firstname) #print John
print(employee001.lastname) #print Doe
print(employee001.pay) #print 80000

conn = sqlite3.connect("employee.db") #Create a connection.  pass a file to store data or an in-memory database sqlite3.connect(":memory").  If the pass a file doesn't exist, sqlite3 creates the pass a file.
createcursor = conn.cursor() #Create a cursor to execute sql commands
createcursor.execute("""create table employeestable
    (firstname text, lastname text, pay integer)""") #write SQL code to create a table
conn.commit()
createcursor.execute("insert into employeestable values ('Corey','Schafer',50000)") #insert a row.  Single quotes in values paranthesis strings.
createcursor.execute("insert into employeestable values ('Mary','Schafer',70000)") #insert a row.  Single quotes in values paranthesis strings.
createcursor.execute("insert into employeestable values (?,?,?)", (employee001.firstname, employee001.lastname, employee001.pay)) #insert a row from class Employee
createcursor.execute("insert into employeestable values (:firstn,:lastn,:payn)", {"firstn": employee002.firstname, "lastn": employee002.lastname, "payn": employee002.pay}) #insert a row from class Employee
createcursor.execute("select * from employeestable where lastname='Schafer'")
# print(createcursor.fetchone()) #prints the first row from select statement as a tuple
# print(createcursor.fetchmany(7)) #prints the first seven rows from select statement as a list with tuples
print(createcursor.fetchall()) #print [('Corey', 'Schafer', 50000), ('Mary', 'Schafer', 70000)].  Prints all the rows from select statement as a list with tuples.
createcursor.execute("select * from employeestable")
print(createcursor.fetchall()) #print [('Corey', 'Schafer', 50000), ('Mary', 'Schafer', 70000), ('John', 'Doe', 80000), ('Jane', 'Doe', 90000)]
createcursor.execute("drop table employeestable") #RM:  delete table to make it easier to run the Python SQLite code from the top
conn.commit()
conn.close() #close connection

testdatabasesavedinram = sqlite3.connect(":memory:") #Create a connection.  pass a file to store data or an in-memory database sqlite3.connect(":memory").  The in-memory database is temporary.  No need to close.  No need to delete at the end.
createcursorinram = testdatabasesavedinram.cursor() #Create a cursor to execute sql commands
createcursorinram.execute("""create table employeestableinram
    (firstname text, lastname text, pay integer)""") #write SQL code to create a table
testdatabasesavedinram.commit()
createcursorinram.execute("insert into employeestableinram values (?,?,?)", (employee001.firstname, employee001.lastname, employee001.pay)) #insert a row from class Employee
createcursorinram.execute("insert into employeestableinram values (:firstn,:lastn,:payn)", {"firstn": employee002.firstname, "lastn": employee002.lastname, "payn": employee002.pay}) #insert a row from class Employee
createcursorinram.execute("select * from employeestableinram")
print(createcursorinram.fetchall()) #print [('John', 'Doe', 80000), ('Jane', 'Doe', 90000)]


basicsqllitepythonway = sqlite3.connect(":memory:") #Create a connection.  pass a file to store data or an in-memory database sqlite3.connect(":memory").  The in-memory database is temporary.  No need to close.  No need to delete at the end.
createcursorinram = basicsqllitepythonway.cursor() #Create a cursor to execute sql commands
createcursorinram.execute("""create table employeestableinrambasic
    (firstname text, lastname text, pay integer)""") #write SQL code to create a table
basicsqllitepythonway.commit()
def insertemployee(inputemployee):
    with basicsqllitepythonway:
        createcursorinram.execute("insert into employeestableinrambasic values (:firstname,:lastname,:pay)", {"firstname": inputemployee.firstname, "lastname": inputemployee.lastname, "pay": inputemployee.pay}) #insert a row
def getemployeesbyname(inputlastname):
    createcursorinram.execute("select * from employeestableinrambasic where lastname=:last", {"last": inputlastname})
    return createcursorinram.fetchall()
def updatepay(inputemployee, inputpay):
    with basicsqllitepythonway:
        createcursorinram.execute("""update employeestableinrambasic set pay = :pay where firstname = :firstname and lastname =:lastname""", {"firstname": inputemployee.firstname, "lastname": inputemployee.lastname, "pay": inputpay})
def removeemployee(inputemployee):
    with basicsqllitepythonway:
        createcursorinram.execute("delete from employeestableinrambasic where firstname =:afirstname and lastname = :alastname", {"afirstname": inputemployee.firstname, "alastname": inputemployee.lastname})
def getallemployees():
    createcursorinram.execute("select * from employeestableinrambasic;")
    return createcursorinram.fetchall()


basicemployee001 = Employee("basicJohn", "basicDoe", 80000)
basicemployee002 = Employee("basicJane", "basicDoe", 90000)
insertemployee(basicemployee001)
insertemployee(basicemployee002)
lastnameemployees = getemployeesbyname("basicDoe")
print(lastnameemployees) #print [('basicJohn', 'basicDoe', 80000), ('basicJane', 'basicDoe', 90000)]
updatepay(basicemployee002, 95555)
removeemployee(basicemployee001)
lastnameemployees = getemployeesbyname("basicDoe")
print(lastnameemployees) #print [('basicJane', 'basicDoe', 95555)]
runfunctiongetallemployees = getallemployees()
print("getallemployes", runfunctiongetallemployees) #print getallemployes [('basicJane', 'basicDoe', 95555)]
