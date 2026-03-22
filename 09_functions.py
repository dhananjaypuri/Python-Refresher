def hello(name):
    return "Hello {}".format(name);

result = hello("Ajay");

print(result);

def show_data(*args, **kwargs):
    print(args);
    print(kwargs);

show_data(1,3, name="Ajay");