"""
Time estimate: 2 hours
Time actual: 1 hour 50 mins

"""

from project import Project
from operator import attrgetter
import datetime

FILENAME = "projects.txt"
MENU = """Menu:  
-(L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""



def main():
    """Manage a list of projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper().strip()

    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)

        elif choice == "S":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            date_string = input("Show projects that start after date (d/m/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)

        elif choice == "A":
            add_project(projects)

        elif choice == "U":
            update_project(projects)

        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(">>> ").upper().strip()


def load_projects(filename):
    """Load projects from a file and return a list of project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)

    return projects


def display_projects(projects):
    """Display projects, sorted and in categories of completion status."""
    incomplete_projects = [project for project in sorted(projects) if not project.is_complete()]
    completed_projects = [project for project in sorted(projects) if project.is_complete()]
    if incomplete_projects:
        print("Incomplete projects:")
        for project in incomplete_projects:
            print("", project)
    if completed_projects:
        print("Completed projects:")
        for project in completed_projects:
            print("", project)

def filter_projects_by_date(projects,date):
    """Filter projects to display only those after a certain date."""
    date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    projects_after_date = [project for project in sorted(projects, key=attrgetter('start_date')) if
                           project.is_after(date)]
    for project in projects_after_date:
        print(project)
    if not projects_after_date:
        print(f"There are no projects that started after {date.strftime("%d/%m/%Y")}")

def get_valid_date(prompt):
    """Get a valid date string from the user, return in date format."""
    valid_date = False
    while not valid_date:
        date_string = input(prompt)
        try:
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            valid_date = True
        except ValueError:
            print("Invalid date")
    return date



def get_user_input():
    """Get user input for a new project and return a Project object."""
    name = input("Project name: ")
    date_string = input("Start date (d/m/yyyy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    """ Allow the user to update the completion percentage and priority of a project."""
    for i, project in enumerate(projects):
        print(i, project)
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_percentage, new_priority)

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"{len(projects)} projects saved to {filename}")

def add_project(projects):
    """Add a new project to the list."""
    project = get_user_input()
    projects.append(project)
    print(f"Project '{project.name}' added.")




if __name__ == "__main__":
    main()

