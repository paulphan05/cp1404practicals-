import datetime

class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name="", start_date=datetime.date.today(), priority=0, cost_estimate=0, completion_percentage=0):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def is_complete(self):
        """Return True if the project is complete (100%), otherwise False."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Allow sorting projects by priority."""
        return self.priority < other.priority
