#coffeesqllitedatabase is from coffeesqllitedatabase.py
import coffeesqllitedatabase as database

def returnrows(rowsasalist):
    for eachrowsasalist in rowsasalist:
        return f"{eachrowsasalist[1]} ({eachrowsasalist[2]}) - {eachrowsasalist[3]}/100"


menuprompt = """-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: """

def menu():
    connection = database.connect()
    database.createtables(connection)
    while (userinput := input(menuprompt)) != "5":  #:= is a walrus to give a variable a value within a statement
        if userinput == "1":
            name = input("Enter bean name: ")
            method = input("Enter how you've prepared it: ")
            rating = int(input("Enter your rating score (0-100): "))
            database.addbean(connection, name, method, rating)
        elif userinput == "2":
            beans = database.getallbeans(connection)
            for eachbeans in beans:
                print(eachbeans)
                print(f"{eachbeans[1]} ({eachbeans[2]}) - {eachbeans[3]}/100")
        elif userinput == "3":
            name = input("Enter bean name to find: ")
            beans = database.getbeansbyname(connection, name)
            print(beans)
            print(returnrows(beans))  #Instructor says create function because printing same as userinput == "2"
        elif userinput == "4":
            name = input("Enter bean name to find: ")
            bestmethod = database.getbestpreparationforbean(connection, name)
            print(bestmethod)
            print(returnrows(bestmethod))
            print("The best preparation method for", name, "is", bestmethod[0][2])  #bestmethod[0][1] is incorrect because the second column index 1 is the coffee name
        else:
            print("Invalid input.  Please try again.")


menu()
'''
-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: 1
Enter bean name: Pink Quality
Enter how you've prepared it: Espresso
Enter your rating score (0-100): 75
-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: 2
(1, 'Awesome Bean 1', 'Expresso', 50)
Awesome Bean 1 (Expresso) - 50/100
(2, 'Pink Quality', 'Espresso', 75)
Pink Quality (Espresso) - 75/100
-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: 3
Enter bean name to find: Awesome Bean 1
[(1, 'Awesome Bean 1', 'Expresso', 50)]
Awesome Bean 1 (Expresso) - 50/100
-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: 4
Enter bean name to find: Pink Quality
[(2, 'Pink Quality', 'Espresso', 75)]
Pink Quality (Espresso) - 75/100
The best preparation method for Pink Quality is Espresso
-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: 5
'''