import re

with open('input.txt', 'r') as f:
    ops = ['(', ')', '+', '*']
    calculations = [[(item if item in ops else int(item)) for item in re.findall(r'[\d+\+\-\*\(\)]', line.strip())] for line in f.readlines()]
    

def calc(step, index=0):
    prev_op=None
    result=None
    while index < len(step):
        item = step[index]
        if item not in ops:
            result = (result+item if prev_op=='+' else  (result*item if prev_op=='*' else item))
            index+=1
        elif item == '(':
            r, index = calc(step, index+1)
            result = (result+r if prev_op=='+' else (result*r if prev_op=='*' else r))
        elif item == ')':
            index+=1
            return result, index
        else:
            prev_op=item
            index+=1      
    return result, index
  
def advanced_calc(step, index=0):
    prev_op=None
    result=None
    while index < len(step):
        item = step[index]
        if item == '*':
            r, index = advanced_calc(step, index+1)
            result*=r
            return result, index
        if item not in ops:
            result = (result+item if prev_op=='+' else  (result*item if prev_op=='*' else item))
            index+=1
        elif item == '(':
            r, index = advanced_calc(step, index+1)
            result = (result+r if prev_op=='+' else (result*r if prev_op=='*' else r))
        elif item == ')':
            index+=1
            return result, index
        else:
            prev_op=item
            index+=1      
    return result, index
            
            
def part1_and_2(calculations, part):
    Sum=0
    for index,line in enumerate(calculations):
        if part==1:
            Sum+=calc(line)[0]
        else:
            Sum+=advanced_calc(line)[0]
    return Sum   

print(part1_and_2(calculations, 1))
print(part1_and_2(calculations, 2))