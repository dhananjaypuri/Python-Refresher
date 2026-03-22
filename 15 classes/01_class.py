class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first;
        self.last = last;
        self.pay = pay;
        self.email = first + '.' + last + '@company.com';

    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee('Ajay', 'Sharma', 5000000);
emp_2 = Employee('Anay', 'Batra', 7000000);

fullname = emp_1.fullname();

print(fullname);


print(Employee.__dict__);



