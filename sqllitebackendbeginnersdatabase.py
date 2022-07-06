import sqlite3

releaselist = [(1997, "Grand Theft Auto", "State Of New Guernsey"), (1999, "Grand Theft Auto 2", "Anywhere, USA"), (2001, "Grand Theft Auto III", "Liberty City"), (2002, "Grand Theft Auto:  Vice City", "Vice City"), (2004, "Grand Theft Auto:  San Andreas", "State Of San Andreas"), (2008, "Grand Theft Auto IV", "Liberty City"), (2013, "Grand Theft Auto V", "Los Santos")]

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("CREATE table if not exists gtatable (releaseyear integer, releasename text, city text);")

cursor.executemany("INSERT into gtatable values (?,?,?);", releaselist)

printgtarows = cursor.execute("SELECT * from gtatable;")
for eachprintgtarows in printgtarows:
    print(eachprintgtarows)
    '''
    (1997, 'Grand Theft Auto', 'State Of New Guernsey')
    (1999, 'Grand Theft Auto 2', 'Anywhere, USA')
    (2001, 'Grand Theft Auto III', 'Liberty City')
    (2002, 'Grand Theft Auto:  Vice City', 'Vice City')
    (2004, 'Grand Theft Auto:  San Andreas', 'State Of San Andreas')
    (2008, 'Grand Theft Auto IV', 'Liberty City')
    (2013, 'Grand Theft Auto V', 'Los Santos')
    '''
#cursor.execute("SELECT * from gtatable where city="Liberty City"") #SyntaxError: invalid syntax
cursor.execute("""
SELECT *
from gtatable
where city = 'Liberty City';
""")

noforlooplibertycity = cursor.fetchall() #Error message for noforlooplibertycity = cursor.fetch() AttributeError: 'sqlite3.Cursor' object has no attribute 'fetch'
print(noforlooplibertycity) #print [(2001, 'Grand Theft Auto III', 'Liberty City'), (2008, 'Grand Theft Auto IV', 'Liberty City')]

cursor.execute("CREATE table if not exists cities (gtacity text, realcity text);")
cursor.execute("INSERT into cities values ('Liberty City','New York');")
cursor.execute("INSERT into cities values (?,?);", ("Vice City", "Miami"))
cursor.execute("INSERT into cities values (?,?);", ("Los Santos", "Los Angeles"))
cursor.execute("SELECT * from cities;")
noforloopprintcities = cursor.fetchall()
print(noforloopprintcities) #print [('Liberty City', 'New York'), ('Vice City', 'Miami'), ('Los Santos', 'Los Angeles')]
attemptajoinblindfaith = cursor.execute("""
SELECT g.releasename, g.city, c.realcity
from gtatable g join cities c
on g.city = c.gtacity;
""")
print(attemptajoinblindfaith) #print <sqlite3.Cursor object at 0x7f03b9f71b20>
print(list(attemptajoinblindfaith)) #print [('Grand Theft Auto III', 'Liberty City', 'New York'), ('Grand Theft Auto:  Vice City', 'Vice City', 'Miami'), ('Grand Theft Auto IV', 'Liberty City', 'New York'), ('Grand Theft Auto V', 'Los Santos', 'Los Angeles')]
attemptaleftjoinblindfaith = cursor.execute("""
SELECT g.releasename, g.city, c.realcity
from gtatable g left join cities c
on g.city = c.gtacity;
""")
for eachattemptaleftjoinblindfaith in attemptaleftjoinblindfaith:
    print(eachattemptaleftjoinblindfaith)
    '''
    ('Grand Theft Auto', 'State Of New Guernsey', None)
    ('Grand Theft Auto 2', 'Anywhere, USA', None)
    ('Grand Theft Auto III', 'Liberty City', 'New York')
    ('Grand Theft Auto:  Vice City', 'Vice City', 'Miami')
    ('Grand Theft Auto:  San Andreas', 'State Of San Andreas', None)
    ('Grand Theft Auto IV', 'Liberty City', 'New York')
    ('Grand Theft Auto V', 'Los Santos', 'Los Angeles')
    '''
print("\n")
#Use for loop to replace Liberty City in gtatable table with New York in cities table using noforlooplibertycity
for i in noforlooplibertycity:
    print(i)
    '''
    (2001, 'Grand Theft Auto III', 'Liberty City')
    (2008, 'Grand Theft Auto IV', 'Liberty City')
    '''
'''
noforloopprintcities = cursor.fetchall()
print(noforloopprintcities) #print [('Liberty City', 'New York'), ('Vice City', 'Miami'), ('Los Santos', 'Los Angeles')]
'''
for i in noforlooplibertycity:
    replacegtacityrealcity = [noforloopprintcities[0][1] if value == noforloopprintcities[0][0] else value for value in i]
    print(replacegtacityrealcity)
    '''
    [2001, 'Grand Theft Auto III', 'New York']
    [2008, 'Grand Theft Auto IV', 'New York']
    '''
printgtarows = cursor.execute("SELECT * from gtatable;")
for i in printgtarows:
    converttupletoalist = [value for value in i]
    print(converttupletoalist)
    '''
    [1997, 'Grand Theft Auto', 'State Of New Guernsey']
    [1999, 'Grand Theft Auto 2', 'Anywhere, USA']
    [2001, 'Grand Theft Auto III', 'Liberty City']
    [2002, 'Grand Theft Auto:  Vice City', 'Vice City']
    [2004, 'Grand Theft Auto:  San Andreas', 'State Of San Andreas']
    [2008, 'Grand Theft Auto IV', 'Liberty City']
    [2013, 'Grand Theft Auto V', 'Los Santos']
    '''

printgtarowssecondtime = cursor.execute("SELECT * from gtatable;")
for i in printgtarowssecondtime:
    print(i)
    '''
    (1997, 'Grand Theft Auto', 'State Of New Guernsey')
    (1999, 'Grand Theft Auto 2', 'Anywhere, USA')
    (2001, 'Grand Theft Auto III', 'Liberty City')
    (2002, 'Grand Theft Auto:  Vice City', 'Vice City')
    (2004, 'Grand Theft Auto:  San Andreas', 'State Of San Andreas')
    (2008, 'Grand Theft Auto IV', 'Liberty City')
    (2013, 'Grand Theft Auto V', 'Los Santos')
    '''
connection.close()
