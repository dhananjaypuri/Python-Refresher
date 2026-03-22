courses = ["AI", "ML", "MLOPS", "DATA SCIENCE"];

print(courses);

print(len(courses));

print(courses[0:2]);

print(dir(courses));

courses.append("Gen AI");

print(courses);

print(courses.insert(2, "Agentic AI"));

print(courses);

new_courses = ["Python", "Fast API"]

courses.extend(new_courses);

print(courses);

courses.remove("Python");

print(courses);

popped = courses.pop();

print(popped);

courses.reverse();

print(courses);

courses.sort();
print(courses);

nums = [1, 10, 0, 98, 89, 12];

nums.sort();

print(nums);

nums.sort(reverse=True);

print(nums);

sorted_nums = sorted(nums);
print(sorted_nums);

print(min(nums));
print(max(nums));
print(sum(nums));

print(courses);
print(courses.index('AI'));

# print(courses.index('Agentic'));

print("AI" in courses);

for crs in courses:
    print(crs);

for ind , crs in enumerate(courses, start=1):
    print(ind , crs);

courses_name = " , ".join(courses);

print("Best courses in AI are : ",courses_name);

text = "abcd";
number = 4;

new_list = [ (i,txt) for i in range(4) for txt in text];

print(new_list);