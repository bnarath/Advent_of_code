import re

with open('input.txt', 'r') as f:
    nav = [inst.strip() for inst in f.readlines()]
    
def calc_Manhattan_part1(nav):
    # east - pos x
    # west - neg x
    # north - pos y
    # south - neg y
    # rotation - L - anti clockwise, R - clockwise
    # rotation_clock = ['E', 'S', 'W', 'N'] - 90 degree is move forward cyclical
    # Ships position - ['FACE', x, y]
    rotation_clock = ['E', 'S', 'W', 'N']
    FACE,x,y='E',0,0
    for instruction in nav:
        inst_decoded = re.findall(r'^(E|S|W|N|F|R|L)(\d+)$', instruction)[0]
        x += (int(inst_decoded[1]) if inst_decoded[0]=='E' else (-1*int(inst_decoded[1]) if inst_decoded[0]=='W' else 0))
        y += (int(inst_decoded[1]) if inst_decoded[0]=='N' else (-1*int(inst_decoded[1]) if inst_decoded[0]=='S' else 0))
        if inst_decoded[0]=='F':
            x+= (int(inst_decoded[1]) if FACE=='E' else (-1*int(inst_decoded[1]) if FACE=='W' else 0))
            y+= (int(inst_decoded[1]) if FACE=='N' else (-1*int(inst_decoded[1]) if FACE=='S' else 0))
        if (inst_decoded[0]=='R') or (inst_decoded[0]=='L'):
            rot_count = int(inst_decoded[1])//90
            FACE=(rotation_clock[(rotation_clock.index(FACE)+rot_count)%len(rotation_clock)] if inst_decoded[0]=='R' else rotation_clock[(rotation_clock.index(FACE)-rot_count)%len(rotation_clock)])
    return abs(x)+abs(y)

def rotate_90(waypoint, direction='R'):
    x, y = waypoint
    if x>=0 and y>=0:
        new_waypoint = ([abs(y), -abs(x)] if direction=='R' else [-abs(y), abs(x)])
    elif x>=0 and y<=0:
        new_waypoint = ([-abs(y), -abs(x)] if direction=='R' else [abs(y), abs(x)])
    elif x<=0 and y<=0:
        new_waypoint = ([-abs(y), abs(x)] if direction=='R' else [abs(y), -abs(x)])
    else:
        new_waypoint = ([abs(y), abs(x)] if direction=='R' else [-abs(y), -abs(x)])
    return new_waypoint


def calc_Manhattan_part2(nav):
    ship = [0,0]
    waypoint = [10,1]
    for instruction in nav:
        inst_decoded = re.findall(r'^(E|S|W|N|F|R|L)(\d+)$', instruction)[0]
        waypoint[0] += (int(inst_decoded[1]) if inst_decoded[0]=='E' else (-1*int(inst_decoded[1]) if inst_decoded[0]=='W' else 0))
        waypoint[1] += (int(inst_decoded[1]) if inst_decoded[0]=='N' else (-1*int(inst_decoded[1]) if inst_decoded[0]=='S' else 0))
        if inst_decoded[0]=='F':
            ship = [ship[index]+(int(inst_decoded[1])*ax) for index, ax in enumerate(waypoint)]
        if (inst_decoded[0]=='R') or (inst_decoded[0]=='L'):
            rot_count = int(inst_decoded[1])//90
            for i in range(rot_count):
                waypoint=rotate_90(waypoint, inst_decoded[0])
    return abs(ship[0])+abs(ship[1])

####part1 - 2847
calc_Manhattan_part1(nav)

####part2 - 29839
calc_Manhattan_part2(nav)