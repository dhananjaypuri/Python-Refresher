class Student:
    
    roll_number = 0;
    def __init__(self, name, subjects):

        print("Creating Student");
        self.name = name;
        self.subjects = subjects;
        Student.roll_number += 1;
        self.roll_number = Student.roll_number

    def display_info(self):

        return f"Student : {self.name} created Successfully .\nRoll Number : {self.roll_number}\n{self.name} is enrolled in Subejects : {" , ".join(self.subjects)}";
        

subjects = ["English", "Maths", "Science"];

st_1 = Student("Ajay", subjects=subjects);
st_2 = Student("Rajan", subjects=subjects);

# st_1.name = "hello";

# print(st_1.__dict__);
# print(Student.__dict__);

print(st_1.display_info());
print("===================================================");
print(st_2.display_info());

