# this is main menue
# ------------------imports----------------------------
import datetime
import project_module
from user_module import User
import re


# ----------------- Register Function ------------------
def register():
    print("Welcome to the registration page!")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    mobile_phone = input("Enter your mobile phone number: ")

    # Validate password
    if password != confirm_password:
        print("Passwords do not match!")
        return

    # check Mobile phone [ validate against Egyptian phone numbers]
    pattern = r"^01[0-2|5]\d{8}$"
    match = re.fullmatch(pattern, mobile_phone)
    if match:
        print("welcome : ", first_name)

    else:
        print(" Is Not valid mobile phone")

    # Create the user object
    user = User(first_name, last_name, email, password, mobile_phone)

    # Save the user object to a file or database
    with open('users.txt', 'a') as f:
        f.write(f"{user.first_name},{user.last_name},{user.email},{user.password},{user.mobile_phone}\n")

    print("Registration successful!")


# ----------------Login function ------------------------------
def login():
    print("Welcome to the login page!")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if the user exists in the file or database
    with open('users.txt', 'r') as f:
        for line in f:
            fields = line.strip().split(',')
            if fields[2] == email and fields[3] == password:
                print("Login successful!")
                project_menu()  # go to project menu
                break
    print("Invalid email or password!")


def main_menu():
    while True:
        print("Welcome to the User Authentication System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


def project_menu():
    while True:
        print("Welcome to the Fundraising App")
        print("1. Create a project")
        print("2. View all projects")
        print("3. Edit a project")
        print("4. Delete a project")
        print("5. Search projects by date")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            project_module.create_project()
        elif choice == "2":
            project_module.display_projects()
        elif choice == "3":
            project_module.edit_project()
        elif choice == "4":
            project_module.delete_project()
        elif choice == "5":
            project_module.search_projects()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


# call main_menu()
main_menu()
