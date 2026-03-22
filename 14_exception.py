
try:
    with open("README.md") as f:
        data = f.read();
        print(data);

except Exception as e:
    print(e);

else:
    print("Try executed correclty");

finally:
    print("This will executes in each and every scenario");