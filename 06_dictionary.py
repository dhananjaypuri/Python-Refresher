courses = ["AI", "ML"];
student = {"name": "Amar", "age": 25, "course": courses};

print(student["name"]);
print(student["age"]);
print(student["course"]);

print("======================================");

for item in student:
    print(student[item]);

print("======================================");

for i,item in enumerate(student):
    print(i,item, student[item]);

print("======================================");
courses.append("GEN AI");
student.update({"phone": 9999999999, "course": courses});

print(student);

print("======================================");

del student['age'];

print(student);

print("======================================");

popped_item = student.pop('phone');

print(popped_item);

print("======================================");

for key in student.keys():
    print(key);

print("======================================");

print(student.items());
for item in student.items():
    print(item[0], " = " , item[1]);

print("======================================");

for k, v in student.items():
    print(k, " = " ,v);