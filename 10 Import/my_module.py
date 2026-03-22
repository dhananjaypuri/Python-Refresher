print("Importing Module");

def greet(name):
    return f"Hi, {name}";

def find_index(main_value, target):
    index = 0;
    if target in main_value:
        index = main_value.index(target);
    else:
        index = -1;

    return index;

