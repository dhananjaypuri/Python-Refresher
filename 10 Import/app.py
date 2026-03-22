# import my_module as mm
from my_module import find_index as fi
nums = [10,100,89,4];

result = fi(nums, 10);

# result = mm.find_index(nums, 10);

if result != -1:
    print(f"Index is {result}");
else:

    print("Target not present in the list");



