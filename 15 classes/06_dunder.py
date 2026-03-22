class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname;
        self.lname = lname;
        self.pay = pay;

    def display_data(self):
        return f"Name: {self.fname} {self.lname}, Salary : {self.pay}";

    def __str__(self):
        return f"{self.fname} {self.lname}";

    def __repr__(self):
        return f'''Employee("{self.fname}", "{self.lname}" , {self.pay})''';

    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee("Ajay", "Yadav", 30000);
emp_2 = Employee("Raghav", "Kumar", 90000);

print(emp_1);
print(repr(emp_1));


print(emp_2);
print(repr(emp_2));

print(emp_1 + emp_2);

print(emp_1.__dict__);