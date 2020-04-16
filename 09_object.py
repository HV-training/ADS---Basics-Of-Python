
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

# creating attributes for every instance
user1 = Developer("john", "williams", "ABC")
user2 = Developer("dave", "smith", "ABC")
user3 = Developer("bob", "mario", "ABC")

print(user1.fullname)

user1.show_details()
user2.show_details()
user3.show_details()






