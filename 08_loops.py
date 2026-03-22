nums = [1,2,3,4,5];

for num in nums:
    print(num);

print("======================================");

for num in nums:
    if num == 2:
        break;
    else:
        print(num);

print("======================================");

for num in nums:
    if num == 2:
        continue;
    else:
        print(num);

print("======================================");

for i in range(1,11):
    print(i);

print("======================================");

x = 0;

while x<10:
    print(x);
    x += 1;