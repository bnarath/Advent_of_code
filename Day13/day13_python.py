import re
import numpy as np
from functools import reduce
import math

with open('input.txt', 'r') as f:
    timings = [line.strip() for line in f.readlines()]
    
def part1(timings):
    arrival = int(timings[0])
    bus_ids = [int(id) for id in timings[1].split(',') if id!='x']
    wait_time = [(((arrival//id)+1)*id) - arrival for id in bus_ids]
    return bus_ids[wait_time.index(min(wait_time))]*min(wait_time)

def calculate_inverse_mod(num, div):
    #######################
    #inverse mode of x mod (k) is the least pos number (n) that gets multiplied with x to produce a remainder of 1 (mod k) after multiplication
    # take x mod k = modx
    # n*modx mod k should be 1 (Go for all multipliers of k , Take +1 and the /by modx)
    # x*num in congruence with 1 mod div => x*modx in congruence with 1 mod div
    modx = num%div
    index = 1
    while (div*index + 1)%modx:
        index+=1
    return (div*index + 1)//modx

def check_if_prime(num):
    if num<=0:
        return False
    elif num in [1,2,3]:
        return True
    else:
        cur = 2
        end = math.ceil(num**(1/2))
        while cur<=end:
            if num%cur == 0:
                return False
            cur+=1
        return True
            
#np.count_nonzero([check_if_prime(num) for num in bus_id_time_constraint])==len(bus_id_time_constraint)  
#All bus intervals are prime => can use CRT

def part2(timings):
    ##Since all arrival epochs are prime, we can use CRT to solve system of congrunces. Take t-1 as the xt (need to find)
    bus_id_time_constraint = {int(val):index for index,val in enumerate(timings[1].split(',')) if val!='x'}
    solve = {key: key-(bus_id_time_constraint[key]+1)%key for key in bus_id_time_constraint}
    M = reduce(lambda x,y : x*y, list(solve.keys()))
    Mis = [M//key for key in solve]
    InverseMis = [calculate_inverse_mod(Mis[index], key) for index,key in enumerate(solve.keys())]
    return sum([Mis[index]*InverseMis[index]*val for index,val in enumerate(solve.values())])%M +1

print(part1(timings))
print(part2(timings))