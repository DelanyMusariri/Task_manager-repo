
# ====Login Section====
passwords = []  # create empty list to add usernames and passwords
with open("user.txt", "r") as f:
    for line in f:
        name_pair = line.strip()
        creds_pair = name_pair.split(", ")
        username = creds_pair[0]  # index 0 to be our username
        password = creds_pair[1]  # index 1 to be our passwords
        creds = (username, password)  # create tuple of username and password
        passwords.append(creds)

user_name = input("Enter your user name :")
password = input("Enter your password :")


while True:  # to repeatedly ask the user to enter the right information
    if (user_name, password) not in passwords:
        print("\nIncorrect password or username please try again :")
        user_name = input("Enter your user name :")  # to enter correct credentials
        password = input("Enter your password :")
    else:
        break

# ========functions section=====
    
def register():
    if user_name != "admin":
        print("Only admin is able to register a user")
    else:
        username = input("Please enter a username :")

        new_password = input("Enter your password :")
        new_password_confirmed = input("please confirm your password :")
        while True:  # repeatedly ask user to input matching passwords
            if new_password != new_password_confirmed:
                print("Passwords do not match, please try again")
                new_password_confirmed = input("confirm your password :")

            else:
                with open("user.txt", "a") as f:
                    new_creds = f"\n{username}, {new_password_confirmed}"
                    f.write(new_creds)
                    print("Complete!")
                    break

def add():
    username = input("What is your user name: ")
    tile_of_task = input("Title of task? ")
    description = input("State the description of the task: ")
    due_date = input("Date of with task is due: ")
    current_date = input("Todays date: ")
    task_complete = input("is the task complete? ")

    with open("tasks.txt", "a") as f:
        new_task = f"\n{username}, {tile_of_task}, {description},\
 {due_date}, {current_date}, {task_complete}"
        f.write(new_task)
        print("Task added!")  # for user satisfaction

def view_all():
    with open("tasks.txt", "r") as f:
        for line in f:
            task_stripped = line.strip()
            task_split = task_stripped.split(", ")
            print(f"Task assigned to: {task_split[0]}\nTask : \
{task_split[1]}\nTask details: {task_split[2]}\nCurrent date : {task_split[3]}\
 \nDue date: {task_split[4]}\nTask complete : {task_split[5]}\n")

def view_mine():
    with open("tasks.txt", "r") as f:
        for lines in f:
            line = lines.strip().split(", ")
            if user_name == line[0]:
                print(f"Task assigned to: {line[0]}\nTask : {line[1]}\
\nTask details: {line[2]}\nCurrent date : {line[3]} \nDue date:\
 {line[4]}\nTask complete? {line[5]}\n")
            else:
                pass

def stats(file1, file2):
    with open(file1, "r") as f:
        num_of_users = 0
        for line in f:
            num_of_users += 1

    with open(file2, "r") as f:
        num_of_tasks = 0
        for line in f:
            num_of_tasks += 1
    
    return (f"The total number of users are: {num_of_users}\nThe total\
 amount of tasks are: {num_of_tasks}")


while True:
    if user_name == "admin":  # make a separate menu for admin
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
s - view stats
: ''').lower()
    else:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        register()

    elif menu == 'a':
        add()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 's':
        print(stats("user.txt", "tasks.txt"))

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
