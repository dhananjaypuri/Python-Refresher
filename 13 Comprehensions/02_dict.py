names = ["Ajay", "Amar", "Anthony", "Vijay"];

numbers = [i+1 for i in range(4)];

print(names);
print(numbers);
new_dict = dict();

for item in zip(numbers , names):
    new_dict[item[0]] = item[1];
print(new_dict);

for num, name in zip(numbers , names):
    new_dict[num] = name;
print(new_dict);

new_dict = {num: name for num,name in zip(numbers , names)}; 

print(new_dict);

new_dict = {num: name for num,name in zip(numbers , names) if name != "Ajay"}; 

print(new_dict);

new_dict = { name: int(len(name)) for name in names };

print(new_dict);

# Create dictionary with even/odd label for numbers

numbers = [1,12,14,15,19,17];

new_dict = { i: "Even" if i % 2 == 0 else "Odd" for i in numbers};

print(new_dict);