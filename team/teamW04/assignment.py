from date import Date
""" CORE REQUIREMENTS """
class Assignment:
    def __init__(self, 
        name="Untitled", 
        start=Date(),
        due=Date(),
        end=Date()):

        self.name = name
        self.start = start
        self.due = due
        self.end = end
    
    def prompt(self):
        self.name = input("Enter a name: ")
        print("\nStart Date:")
        self.start.prompt()
        print("\nDue Date:")
        self.due.prompt()
        print("\nEnd Date:")
        self.end.prompt()

    def display(self):
        print(f"""\nAssignment: {self.name}\nStart Date:""")
        self.start.display()
        print("Due Date:")
        self.due.display()
        print("End Date:")
        self.end.display()

    """ STRETCH CHALLENGES """
    def display_long(self):
        print(f"""\nAssignment: {self.name}\nStart Date:""")
        self.start.display_long()
        print("Due Date:")
        self.due.display_long()
        print("End Date:")
        self.end.display_long()