import sqlite3
# creating and connecting to the database
conn = sqlite3.connect('tracker.db')
c = conn.cursor()

# creating the tables
c.execute("""CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        expense TEXT ,
        cost INTEGER,
        category TEXT
)""")


c.execute("""CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        income TEXT ,
        amount INTEGER,
        category TEXT
)""")

c.execute("""CREATE TABLE IF NOT EXISTS budget (
        category TEXT PRIMARY KEY,
        amount INTEGER
)""")

c.execute("""CREATE TABLE IF NOT EXISTS goals (
        date TEXT ,
        amount_added INTEGER
)""")

conn.commit()


# functions
# ------add to tables functions-------
# -adding_expense()
# -adding_income()
# -set_budget()
# -adding_to goal()

# For the functions mentioned above
# while true loop is to repeatedly prompt user to enter the right value
# then the try block comes next... this is for error handling
# then comes the input values added to variables
# variables are then added to a tuple if there are more than 2 values
# the execute query follows inserting values from the inputs to the table
# a message follows for user satisfaction showing the process is done
# the except block is part of the try block showing the error message to user

# ------viewing functions--------
# -view_expenses()
# -view_exp_category()
# -view_income()
# -view_inc_category()
# -view_budget()
# -view_progress()

# For the functions mentioned above
# the function will start with an execute query selecting all values from table
# if there is nothing thats where the "if not" block comes in
# else the next execute query is to select all from the table to view
# then the contents is made readable with code to print as a string

# other viewing functions first shows the the different categories
# this is done through the "distinct" query
# follows th "if not" block incase there are no categories existing
# with code makes list to a string for readability if there are existing categories
# the else block follows the categories are shown and a message
# message asks user what category they would like to view from the ones given
# and assigned to a variable
# the "if not" is for error handling if user enters non existent category
# then from the value entered the execute query is set to view category contents
# and more code to convert the list to string

# ---------------------
# error handling is wrapped in a loop like the try and except block


def adding_expense():
    while True:  # to repeatedly prompt user to enter the right value
        try:  # try block for error handling
            exp_name = input("what is the expense name: ").capitalize()
            exp_amount = int(input("amount due: "))
            exp_cat = input("what category does it fall under? ").lower()
            add_creds = [(exp_name, exp_amount, exp_cat)]
            # the above are inputs to add into the table

            c.executemany("""INSERT INTO expenses(expense, cost, category)
                    VALUES (?,?,?)""", add_creds)  # entering the values given
            conn. commit()
            print("Expense successfully added")
            break

        except ValueError:  # error that pops out when given wrong values
            print("please enter an amount")


def view_expenses():
    c.execute('SELECT * FROM expenses')  # distinct is to show unique values
    show = c.fetchall()
    print("\nID: expense: amount: category")
    if not show:  # error handling incase there is nothing in the table
        print("no expenses yet\n")
    else:
        for i in show:  # making the result readable from being a list
            result = " | ".join(str(item) for item in (i))
            print(result)
    return print("Done\n")


def view_exp_category():
    c.execute("SELECT DISTINCT category FROM expenses")
    # distinct is to show unique values

    categories = c.fetchall()
    print("\navailable categories:")
    if not categories:  # error handling incase there is nothing in the table
        print("no categories available yet\n")

    else:
        for i in categories:  # making the result readable from being a list
            category = " ".join(i)
            print(category)

        creds = []
        for i in categories:
            new = " ".join(i)
            creds.append(new)

        while True:
            # asking user to enter values to add into table
            cat = input("\nWhat category would you like to view: ").lower()
            if cat not in creds:
                # error handling incase there is nothing in the table
                print("This category does not exist")
            else:
                print("\nID: expense: amount: category")
                c.execute("SELECT * FROM expenses WHERE category = (?)", (cat,))
                show = c.fetchall()
                for i in show:  # making the result show as string
                    result = " | ".join(str(item) for item in i)
                    print(result)
                return print("Done\n")


def adding_income():
    while True:  # to repeatedly prompt user to enter the right value
        try:  # try block for error handling
            inc_name = input("what is the income name: ").capitalize()
            inc_amount = int(input("amount receivable: "))
            inc_cat = input("what category does it fall under? ").lower()
            add_creds = [(inc_name, inc_amount, inc_cat)]
            # gathering input to enter into table

            c.executemany("""INSERT INTO income(income, amount, category)
                          VALUES (?,?,?)""", add_creds)
            # entering into table

            conn. commit()
            print("Income successfully added")
            break

        except ValueError:  # error that will pop up
            print("please enter an amount")


def view_income():
    c.execute('SELECT * FROM income')
    show = c.fetchall()
    print("\nID: Income: amount: category")
    if not show:
        print("no income yet\n")
    else:
        for i in show:
            result = " | ".join(str(item) for item in i)
            print(result)
        return print("\nDone")


def view_inc_category():
    c.execute("SELECT DISTINCT category FROM income")
    categories = c.fetchall()
    print("\navailable categories:")
    if not categories:
        print("no categories available yet\n")

    else:
        for i in categories:
            category = " ".join(i)
            print(category)

        creds = []
        for i in categories:
            new = " ".join(i)
            creds.append(new)

        while True:
            cat = input("\nWhat category would you like to view: ").lower()
            if cat not in creds:
                print("this category does not exist")
            else:
                c.execute('SELECT * FROM income WHERE category = (?)', (cat,))
                show = c.fetchall()
                print(f"\n{cat} table:")
                for i in show:
                    result = " | ".join(str(item) for item in i)
                    print(result)
                return print("\nDone")


def set_budget():
    while True:
        try:
            category = input("what category would you like to set? ").lower()
            amount = int(input("how much would you like to set it to? "))
            bud_set = (category, amount)
            c.execute("INSERT INTO budget VALUES (?,?)", bud_set)
            conn.commit()
            print("budget set")
            break

        except ValueError:
            print("please enter a number")


def view_budget():
    c.execute("SELECT DISTINCT category FROM budget")
    categories = c.fetchall()
    print("available categories:")
    if not categories:
        print("\nno categories available yet")

    else:
        for i in categories:
            category = " ".join(str(item) for item in (i))
            print(category)

        creds = []
        for i in categories:
            new = " ".join(i)
            creds.append(new)

        while True:
            cat = input("\nwhat category budget would you like to view? ").lower()
            if cat not in creds:
                print("this category does not exist, please try again: ")
            else:
                c.execute("SELECT * FROM budget WHERE category = (?)", (cat,))
                print("\ncategory: amount")
                show = c.fetchall()
                for i in show:
                    result = " | ".join(str(item) for item in (i))
                    print(f"{result}\n")
                return print("\nDone")


def set_goal():
    while True:
        try:
            goal = int(input("how much would you like your goal to be? "))
            print(f"your goal will amount to R{goal}\nGoal successfully set.")
            break

        except ValueError:
            print("please enter an amount: ")


def adding_to_goal():
    while True:
        try:
            amount = int(input("How much are you adding to your progress? "))
            date = input("Todays date? ")
            break

        except ValueError:
            print("please enter an amount and the correct date")

    c.execute(" INSERT INTO goals VALUES (?,?)", (date, amount))
    print("Amount successfully added")
    conn.commit()


def view_progress():
    c.execute("SELECT * FROM goals")
    show = c.fetchall()
    if not show:
        print("no progress as of yet")

    else:
        print("\nDate added: amount")
        for i in show:
            result = " | ".join(str(item) for item in (i))
            print(result)

        print("You are doing well reaching your goal keep it up")


# menu
while True:  # loop to iterate menu till the exit function is hit
    while True:  # loop to iterate error message till correct values are given
        try:  # error handling for invalid inputs from user
            menu = int(input("""
1. Add expense
2. View expenses
3. View expenses by category
4. Add income
5. View income
6. View income by category
7. Set budget for a category
8. View budget for a category
9. Set financial goals
10. Add to goals
11. View progress towards financial goals
12. Quit: """))
            break  # break loop

        # exception handling ...error messages that pop up when theres an error
        except ValueError:
            print("please enter a number from the menu")
        except Exception:
            print("Something went wrong please enter a number from the menu")

    if menu == 1:
        adding_expense()
    elif menu == 2:
        view_expenses()
    elif menu == 3:
        view_exp_category()
    elif menu == 4:
        adding_income()
    elif menu == 5:
        view_income()
    elif menu == 6:
        view_inc_category()
    elif menu == 7:
        set_budget()
    elif menu == 8:
        view_budget()
    elif menu == 9:
        set_goal()
    elif menu == 10:
        adding_to_goal()
    elif menu == 11:
        view_progress()
    elif menu == 12:
        break

    else:
        print("You have entered an invalid input. Please try again")

conn.commit()  # to commit any final uncommitted queries
conn.close()  # to close of the  sqlite program
