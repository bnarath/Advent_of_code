with open('input.txt', 'r') as f:
    numbers = [int(number.strip()) for number in f.readlines()]

def check_if_sum_of_two_prev(num, list_of_numbers):
    for number in list_of_numbers:
        if (num-number in numbers) and (number!=(num-number)):
            return True
    return False
def check_the_anomaly_number():
    for index, num in enumerate(numbers[25:]):
        if not check_if_sum_of_two_prev(num, numbers[index:index+25:]):
            return num
    return "All numbers satisfy the requirement"

def check_contiguous_sum_equate(size, cont_range, num):
    lb, ub, start = 0, len(cont_range), 0
    while start+size <= ub:
        if sum(cont_range[start:start+size])==num:
            return (min(cont_range[start:start+size]), max(cont_range[start:start+size]))
        start+=1
    return False

def find_min_max_cont_range():
    anomaly = check_the_anomaly_number()
    index_of_anomaly = numbers.index(check_the_anomaly_number())
    done,size = False, 2
    while size<=max(index_of_anomaly, len(numbers)-index_of_anomaly-1):
        if size<= index_of_anomaly:
            lower = check_contiguous_sum_equate(size, numbers[:index_of_anomaly], anomaly)
            if lower: return lower
        if size<= len(numbers)-index_of_anomaly-1:
            upper = check_contiguous_sum_equate(size, numbers[index_of_anomaly+1:], anomaly)
            if upper: return upper
        size+=1
    return "No contiguous range found"

###part1 - 1038347917
print(check_the_anomaly_number())
###part2 - 137394018
print(sum(find_min_max_cont_range()))