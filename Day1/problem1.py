import os
import numpy as np


with open('problem1_input.txt', 'r') as f:
    numbers = f.readlines()

numbers = np.array([int(num) for num in numbers])
numbers_rotate = numbers.copy()
done = np.where(numbers + numbers_rotate == 2020)[0]
iter = 1
while (not done.size) and (iter < len(numbers)):
    print(iter)
    numbers_rotate = np.roll(numbers_rotate, 1)
    done = np.where(numbers + numbers_rotate == 2020)[0]
    iter +=1

if done.size > 0: 
    print(numbers[done], numbers_rotate[done], numbers[done]*numbers_rotate[done]) 
else: 
    print("No pair sums up to 2020")

