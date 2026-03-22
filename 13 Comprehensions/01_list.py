nums = [1,2,8,4];

new_nums = [ num**2 for num in nums];

print(new_nums);

print("Print even");
# even_numbers = [f"{num} is Even" if num % 2 == 0 else f"{num} is Odd" for num in nums]
even_numbers = [ f"{num} is Even" if num % 2 == 0 else "odd" for num in nums  ];

print(even_numbers);

print("Print Odd");

odd_numbers = [ f"{num} is Odd" for num in nums if num % 2 != 0 ];

print(odd_numbers);

print("Print All");

numbers = [f"{num} is Even" if num % 2 == 0 else f"{num} is Odd" for num in nums]

print(numbers);