import numpy as np
input_file = 'problem1_input.txt'
with open(input_file, 'r') as f:
    numbers = f.readlines()
numbers = np.array([int(num) for num in numbers])
print(numbers + numbers[:, None])

# solution_1 = np.product(numbers[np.unique(np.where((numbers + numbers[:, None] == 2020)))])
# print(f"Solution 1: {solution_1}")
# solution_2 = np.product(numbers[np.unique(np.where((numbers + numbers[:, None] + numbers[:, None, None] == 2020)))])
# print(f"Solution 2: {solution_2}")