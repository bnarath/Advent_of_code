Input = [5,2,8,16,18,0,1]
from tqdm import tqdm
def find_the_num_spoken(Input,turn=30000000):
    num_spoken_time_stamps = {} #Spoken num : [count, [2nd last, last]]
    for i in tqdm(range(turn)):
        count, last_turn = 0, [-1, i]
        if i < len(Input):
            if Input[i] in num_spoken_time_stamps:
                count, last_turn = num_spoken_time_stamps[Input[i]]
                last_turn=last_turn[::-1]
                last_turn[-1]=i
            num_spoken_time_stamps[Input[i]] = [count+1, last_turn]
            last = Input[i]
        else:
            if num_spoken_time_stamps[last][0]>1:
                count, last_turn = num_spoken_time_stamps[last]
                number = last_turn[1]-last_turn[0]
            else:
                number = 0
            count, last_turn = 0, [-1, i]
            if number in num_spoken_time_stamps:
                count, last_turn = num_spoken_time_stamps[number]
                last_turn=last_turn[::-1]
                last_turn[-1]=i
            last = number
            num_spoken_time_stamps[number] = [count+1, last_turn]
    return last