tuple_1 = (1,2,3);

tuple_2 = tuple_1;

print(tuple_1);
print(tuple_2);

for item in tuple_1:
    print(item);

for ind, item in enumerate(tuple_1, start=1):
    print(ind , item);

print(tuple_1[0]);
print(tuple_1[0:]);
print(tuple_1[0:len(tuple_1)-1]);

print(dir(tuple_1));

print(tuple_1.count(1));
print(tuple_1.index(1));
