#This is project module
import datetime


class Project:
    def __init__(self, title, details, total_target, start_time, end_time):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.title}, {self.details}, {self.total_target}, {self.start_time}, {self.end_time}"


def create_project():
    # Prompt the user to enter project details
    title = input("Enter the project title: ")
    details = input("Enter the project details: ")
    total_target = int(input("Enter the total target amount: "))
    start_time = input("Enter the start time (YYYY-MM-DD): ")
    end_time = input("Enter the end time (YYYY-MM-DD): ")

    # Validate the start and end times using the datetime module
    try:
        start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d").date()
        end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    # Create the project object
    project = Project(title, details, total_target, start_time, end_time)
    # Save the project object to a file or database
    with open('projects.txt', 'a') as f:
        f.write(f"{project.title},{project.details},{project.total_target},{project.start_time},{project.end_time}\n")

    print("Project created successfully!")


def display_projects():
    print("All projects:")
    with open('projects.txt', 'r') as f:
        for line in f:
            fields = line.strip().split(',')
            project = Project(fields[0], fields[1], fields[2], fields[3], fields[4])
            print(project)


def edit_project():
    print("Welcome to the edit project page!")
    title = input("Enter the project title: ")

    # Find the project in the file or database
    with open('projects.txt', 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        fields = line.strip().split(',')
        if fields[0] == title:
            project = Project(fields[0], fields[1], int(fields[2]), fields[3], fields[4])
            break
    else:
        print("Project not found!")
        return

    # Prompt the user to enter the new information
    new_title = input(f"Enter the new title ({project.title}): ") or project.title
    new_details = input(f"Enter the new details ({project.details}): ") or project.details
    new_total_target = input(f"Enter the new total target ({project.total_target}): ") or project.total_target
    new_start_time = input(f"Enter the new start time ({project.start_time}): ") or project.start_time
    new_end_time = input(f"Enter the new end time ({project.end_time}): ") or project.end_time

    # Validate start/end time
    try:
        new_start_time = datetime.datetime.strptime(new_start_time, '%Y-%m-%d ').date()
        new_end_time = datetime.datetime.strptime(new_end_time, '%Y-%m-%d ').date()
    except ValueError:
        print("Invalid date format!")
        return

    # Update the project object
    project.title = new_title
    project.details = new_details
    project.total_target = int(new_total_target)
    project.start_time = new_start_time
    project.end_time = new_end_time

    # Update the project information in the file or database
    lines[i] = f"{project.title},{project.details},{project.total_target},{project.start_time},{project.end_time}\n"
    with open('projects.txt', 'w') as f:
        f.writelines(lines)

    print("Project updated successfully!")


def delete_project():
    print("Welcome to the delete project page!")
    title = input("Enter the project title: ")

    # Find the project in the file or database
    with open('projects.txt', 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        fields = line.strip().split(',')
        if fields[0] == title:
            del lines[i]
            break
    else:
        print("Project not found!")
        return

    # Update the project information in the file or database
    with open('projects.txt', 'w') as f:
        f.writelines(lines)

    print("Project deleted successfully!")


def search_projects():
    print("Welcome to the search project page!")
    start_time = input("Enter the start time (YYYY-MM-DD ): ")
    end_time = input("Enter the end time (YYYY-MM-DD ): ")

    # Validate start/end time
    try:
        start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d").date()
        end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format!")
        return

    # Search for projects within the specified time range
    print("Search results:")
    with open('projects.txt', 'r') as f:
        for line in f:
            fields = line.strip().split(',')
            project = Project(fields[0], fields[1], fields[2], fields[3], fields[4])

            print(project)
