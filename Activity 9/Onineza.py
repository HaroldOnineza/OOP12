class Employee:
    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number

    def __str__(self):
        return f"Employee(name='{self.name}', email='{self.email}', mobile_number='{self.mobile_number}')"

# Instantiate the Employee class 2 times
employee1 = Employee("Jeysever", "jeysever@gmail.com", "+639540772644")
employee2 = Employee("Merck Bajane", "merck_Bajane@yahoo.com", "+639425795210")

# Display all properties
print(employee1)
print(employee2)
