course1 = {"AI", "ML", "DL"};
course2 = {"AI", "DATA SCIENCE", "DL", "GEN AI", "AGENTIC AI"};

for crs in enumerate(course1):
    print(crs);

print(course1.union(course2));
print(course1.difference(course2));
print(course1.intersection(course2));
