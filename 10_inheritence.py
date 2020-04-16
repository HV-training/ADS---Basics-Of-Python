
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""


class Developer:
    # class variables for all instances
    bonus = "Yes"
    def __init__(self, fname, lname, company):
        # instance variables unique to each instance
        self.fname = fname
        self.lname = lname
        self.email_id = fname + lname + "@" + company + ".com"
        self.company = company
        self.fullname = self.fname + " " + self.lname

    def show_details(self):
        return self.fullname, self.email_id, Developer.bonus

class Manager(Developer):
    def __init__(self, fname, lname, company, salary):
        super().__init__(fname, lname, company)
        self.salary = salary
        self.bonus = salary * 0.2

    def total_salary(self):
        self.total_salary = self.salary + self.bonus
        return self.total_salary

user1 = Manager("john", "williams", "ABC", 70000)
user2 = Manager("dave", "smith", "ABC", 125000)
user3 = Manager("bob", "mario", "ABC", 80000)

print(user1.fullname)
print(user2.fullname)
print(user3.show_details())


# Assignment - 10

