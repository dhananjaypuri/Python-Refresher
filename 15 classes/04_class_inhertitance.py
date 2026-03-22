class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname;
        self.lname = lname;
        self.email = f"{fname}.{lname}@company.com";
        self.pay = pay

    def display_emp(self):
        return f"New Employee Created with below details.\nName: {self.fname} {self.lname}\nEmail: {self.email}\nPay: {self.pay}";

class Developer(Employee):
    def __init__(self, fname, lname, pay, lang):
        super().__init__(fname, lname, pay);
        self.lang = lang;

    def display(self):
        data = super().display_emp();
        return f"{data}\nProgramming Language: {self.lang}";
    
class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        print("Adding Manager");
        super().__init__(fname, lname, pay);
        if employees is None:
            self.employees = [];
        else:
            self.employees = employees;

    def disp_man_data(self):
       data = super().display_emp();
       emp_data = "";
       if len(self.employees)>0:
           for emp in self.employees:
               emp_data = emp_data + emp.fname + "\n";
       else:
           emp_data = f"Manager {self.fname} has no employee .";

       return f"{data}\n{emp_data}";

    def add_emp(self, emp):
        self.employees.append(emp);
        return f"Employee added successfully under {self.fname}";

dev_1 = Developer("Ajay", "Sharma", 12000, "Python");
dev_2 = Developer("Ashu", "Verma", 13000, "JAVA");

man_1 = Manager("Vijay", "Yadav", "90000", [dev_1]);

print(man_1.disp_man_data());
print(man_1.add_emp(dev_2));
print(man_1.disp_man_data());




