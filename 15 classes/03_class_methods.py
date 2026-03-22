class Employee:
    company = "Apple";

    def __init__(self, name):
        print("New employee created");
        self.name = name;

    def show(self):
        return f"Name: {self.name}\nCompany Name: {self.company}";

    @classmethod
    def changeCompany(cls, new):
        cls.company = new
    
emp_1 = Employee("Ajay");

# print(emp_1.__dict__);
# print(Employee.__dict__);

print(emp_1.show());
print("========================================================");
emp_1.changeCompany("Tesla");

print(Employee.company);
print(emp_1.show());
