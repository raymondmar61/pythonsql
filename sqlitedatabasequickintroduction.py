import sqlite3

db = sqlite3.connect("books.db") #Connect to the database.  If the database doesn't exist, then sqlite3 creates the database; otherwise, sqllite3 connects to the existing database.
cur = db.cursor() #The cursor enables us to work with the database.  Plain English.
cur.execute("""
CREATE table if not exists books
(id integer primary key, title text not null, author not null, price real);
""")
cur.execute("""
INSERT into books(id, title, author, price)
values(1,"Untold Stories","Alan Bennett",17.49);
""")
bookslistinsertmultiplevalues = [(2, "Lucky Jim", "Kingsley Amis", 4.99), (3, "Animal Farm", "George Orwell", 7.49), (4, "Why I Am So Clever", "Friedrich Nietzsche", 1.11), (5, "Human Compatible:  AI and the Problem of Control", "Stuart Russell", 21.49), (6, "Life 3.0:  Being Human in the Age of Artifical . . . ", "Max Tegmark", 9.99), (7, "Superintelligence:  Path, Dangers, Strategies", "Nick Bostrom", 8.49)]
cur.executemany("""
INSERT into books(id, title, author, price)
values(?,?,?,?)
""", bookslistinsertmultiplevalues)

cur.execute("""
SELECT *
from books
order by title;
""")
print(cur.fetchall()) #print [(3, 'Animal Farm', 'George Orwell', 7.49), (5, 'Human Compatible:  AI and the Problem of Control', 'Stuart Russell', 21.49), (6, 'Life 3.0:  Being Human in the Age of Artifical . . . ', 'Max Tegmark', 9.99), (2, 'Lucky Jim', 'Kingsley Amis', 4.99), (7, 'Superintelligence:  Path, Dangers, Strategies', 'Nick Bostrom', 8.49), (1, 'Untold Stories', 'Alan Bennett', 17.49), (4, 'Why I Am So Clever', 'Friedrich Nietzsche', 1.11)]
cur.execute("""
SELECT *
from books;
""")
variabledatabaserows = cur.fetchall()  #RM:  Need another cur.execute function to print each row for the for loop.  Can't reuse the initial cur.execute() order by title.
for eachrow in variabledatabaserows:
    print(eachrow)
    '''
    (1, 'Untold Stories', 'Alan Bennett', 17.49)
    (2, 'Lucky Jim', 'Kingsley Amis', 4.99)
    (3, 'Animal Farm', 'George Orwell', 7.49)
    (4, 'Why I Am So Clever', 'Friedrich Nietzsche', 1.11)
    (5, 'Human Compatible:  AI and the Problem of Control', 'Stuart Russell', 21.49)
    (6, 'Life 3.0:  Being Human in the Age of Artifical . . . ', 'Max Tegmark', 9.99)
    (7, 'Superintelligence:  Path, Dangers, Strategies', 'Nick Bostrom', 8.49)
    '''
cur.execute("""
SELECT *
from books
where price >10;
""")
print(cur.fetchall()) #print [(1, 'Untold Stories', 'Alan Bennett', 17.49), (5, 'Human Compatible:  AI and the Problem of Control', 'Stuart Russell', 21.49)]
print(type(cur.fetchall())) #print <class 'list'>
cur.execute("""
SELECT author
from books;
""")
variabledatabaserowsauthoronly = cur.fetchall()  #RM:  Need another cur.execute function to print each row for the for loop.  Can't reuse the previous cur.execute().
print(type(variabledatabaserowsauthoronly)) #print <class 'list'>
for eachrow in variabledatabaserowsauthoronly:
    print(eachrow)
    print(type(eachrow))
    '''
    ('Alan Bennett',)
    <class 'tuple'>
    ('Kingsley Amis',)
    <class 'tuple'>
    ('George Orwell',)
    <class 'tuple'>
    ('Friedrich Nietzsche',)
    <class 'tuple'>
    ('Stuart Russell',)
    <class 'tuple'>
    ('Max Tegmark',)
    <class 'tuple'>
    ('Nick Bostrom',)
    <class 'tuple'>
    '''
db.commit()
db.close() #Close the connection to the database

import sqlite3
import pandas as pd

db = sqlite3.connect("books.db") #Connect to the database.  If the database doesn't exist, then sqlite3 creates the database; otherwise, sqllite3 connects to the existing database.
data = pd.read_sql_query("SELECT * from books;", db)
print(data)
'''
   id  ...  price
0   1  ...  17.49
1   2  ...   4.99
2   3  ...   7.49
3   4  ...   1.11
4   5  ...  21.49
5   6  ...   9.99
6   7  ...   8.49

[7 rows x 4 columns]
'''
print(data.head())
'''
   id  ...  price
0   1  ...  17.49
1   2  ...   4.99
2   3  ...   7.49
3   4  ...   1.11
4   5  ...  21.49

[5 rows x 4 columns]
'''
insertrowbook = {"id": 12, "author": "P.G. Wodehouse", "title": "Luck of the Bodkins", "price": 6.49}
data = data.append(insertrowbook, ignore_index=True)
print(data)
'''
   id  ...  price
0   1  ...  17.49
1   2  ...   4.99
2   3  ...   7.49
3   4  ...   1.11
4   5  ...  21.49
5   6  ...   9.99
6   7  ...   8.49
7  12  ...   6.49

[8 rows x 4 columns]
'''
data.to_sql("books", db, if_exists="replace", index=False) #save to the SQLite database