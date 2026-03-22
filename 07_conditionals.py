language = "Java";

if language == "Python":
    print("Language is Python");
if language == "Java":
    print("Language is Java");
else:
    print("No Match");

def ret_data(data):
    if len(data)> 0:
        return data;
    else:
        return [];

list_data = [];

# print(ret_data(list_data));

if ret_data(list_data) == []:
    print("Empty List");
else:
    print(ret_data(list_data));


list2 = [];

def retdata(data):
    return data;

if retdata(list2):
    print("Has data");
else:
    print("No data");