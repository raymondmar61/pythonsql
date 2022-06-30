'''
#Database is coffee named beans
id,name,method,rating
1,Peruvian Masters,Percolator,85
2,Pink Quality,Espresso,75
3,Awesome Arabica,Espresso,90
4,Raw Unroasted Beans,Percolator,5
5,Exclusive Blend,Filter,65

#Quick SQL lesson
create table if not exists beans(id integer primary key, name text, method text, rating integer);
insert into beans
values(1, 'Exclusive Blend', 'Percolator', 65);
select *
from beans
where name = 'Exclusive Blend'
order by rating desc;
select method, rating
from beans
order by rating desc limit 1;
select method, avg(rating)
from beans
group by method;
'''
import sqlite3

#YouTuber suggested write SQL first
createbeanstable = "CREATE TABLE if not exists beans (id integer primary key, name text, method text, rating integer);"
insertbean = "INSERT INTO beans (name, method, rating) values(?, ?, ?);"
getallbeanssql = "SELECT * from beans;"
getbeansbynamesql = "SELECT * from beans where name = ?;"
getbestpreparationforbeansql = """
SELECT *
from beans
where name = ?
order by rating desc
limit 1;
"""

#Connect to the database
def connect():
    return sqlite3.connect("datacoffee.db")


#Create a table.
def createtables(connection):
    with connection:
        connection.execute(createbeanstable)

#Add data is saved to the database file
def addbean(connection, name, method, rating):
    with connection:
        connection.execute(insertbean, (name, method, rating))

#Execute SQL queries
def getallbeans(connection):
    with connection:
        return connection.execute(getallbeanssql).fetchall() #get a list of rows returned by the database
def getbeansbyname(connection, name):
    with connection:
        return connection.execute(getbeansbynamesql, (name,)).fetchall() #get a list of rows returned by the database.  RM:  The comma needed in (name,) tells user it's a tuple.
def getbestpreparationforbean(connection, name):
    with connection:
        #return connection.execute(getbestpreparationforbeansql, (name,)).fetchone() #returns a tuple
        return connection.execute(getbestpreparationforbeansql, (name,)).fetchall() #returns a list.  RM:  I need to return a list because of the function returnrows
