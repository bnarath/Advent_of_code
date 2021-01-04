from collections import Counter
import numpy as np

with open('input.txt', 'r') as f:
    adapter_voltages = [int(number.strip()) for number in f.readlines()]
    
#Sort in ascending order and find the volt diff    
sorted_adapter_voltages = sorted(adapter_voltages)
sorted_adapter_voltages = [0] + sorted_adapter_voltages + [sorted_adapter_voltages[-1]+3]
voltage_diff = [ada-sorted_adapter_voltages[index-1] for index, ada in enumerate(sorted_adapter_voltages) if index!=0]

#All possible list of the contigues ones
def count_cont_ones(voltage_diff):
    count_ones_list = []
    count=0
    for val in voltage_diff:
        if val==1:
            count+=1
        else:
            if count:
                count_ones_list.append(count)
                count=0
    return count_ones_list
count_ones_list = count_cont_ones(voltage_diff)

#Count the number of permulations for a contiguous volt diff of 1's
def check_valid_combinations(length):
    valid_combinations = 0
    for num in range(2**length):
        combination = [int(d) for d in (length-len(str(bin(num))[2:]))*'0' + str(bin(num))[2:]]
        if sum(combination):
            #print(combination)
            diff = [-1]+[index for index,val in enumerate(combination) if val==1]+[length+2]
            if max([d-diff[i] for i,d in enumerate(diff[1:])]) <= 3:
                valid_combinations+=1
    return valid_combinations
valid_combination_count_dict = {key:check_valid_combinations(key) for key in Counter(count_ones_list)}

#Find the count of all the combinations
def count_combinations():
    unique_combinations = 1
    counter = Counter(count_ones_list)
    for key in counter:
        unique_combinations*=valid_combination_count_dict[key]**counter[key]
    return unique_combinations

####part1
print(np.prod(list(Counter(voltage_diff).values())))

####part2
print(count_combinations())