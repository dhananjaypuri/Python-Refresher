class Student:

    def __init__(self, fname, lname):
        self.fname = fname;
        self.lname = lname;
        
    @property
    def fullname(self):
        return f"{self.fname} {self.lname}";

    @fullname.setter
    def fullname(self, name):
        self.fname = name.split(' ')[0];
        self.lname = name.split(' ')[1];
        # return f"{self.fname} {self.lname}";

    @property
    def mail(self):
        self.email = f"{self.fname}.{self.lname}@company.com";
        return self.email;


    def __repr__(self):
        return f"Student(\"{self.fname}\",\"{self.lname}\")";

    def __str__(self):
        return f"{self.fname} {self.lname} : {self.mail}"
    
emp_1 = Student("Ajay", "Sharma");

emp_1.fname = "Rishi";

print(repr(emp_1));
print(emp_1.fullname);
print(emp_1);

emp_1.fname = "Ram";
print(repr(emp_1));
print(emp_1.fullname);
print(emp_1);

emp_1.fullname = "Akhil Kumar";
print(repr(emp_1));
print(emp_1.fullname);
print(emp_1);


