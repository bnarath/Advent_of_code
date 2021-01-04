import os
import numpy as np


with open('problem1_input.txt', 'r') as f:
    numbers = f.readlines()

numbers = np.array([int(num) for num in numbers])
numbers_rotate1 = numbers.copy()
numbers_rotate2 = numbers.copy()
done = np.where(numbers + numbers_rotate1 + numbers_rotate2  == 2020)[0]
iter1 = 1
while (not done.size) and (iter1 < len(numbers)):
    iter2 = 1
    while (not done.size) and (iter2 < len(numbers)):                                                                                        
        numbers_rotate2 = np.roll(numbers_rotate2, 1)
        done = np.where(numbers + numbers_rotate1 + numbers_rotate2 == 2020)[0]
        iter2 +=1 
    if (not done.size):
        numbers_rotate1 = np.roll(numbers_rotate1, 1)   
    iter1 +=1

if done.size > 0: 
    print(numbers[done], numbers_rotate1[done],  numbers_rotate2[done], numbers[done]*numbers_rotate1[done]*numbers_rotate2[done]) 
else: 
    print("No pair sums up to 2020")

