import re
import numpy as np
from functools import reduce
from itertools import permutations


def parse(file):
    rule = {}
    yourTicketFlag = False
    nearbyTicketsFlag = False
    nearbyTickets = []
    yourTicket = None
    for line in file:
        match_grp = re.findall(r'^([a-z\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$', line.strip())
        if match_grp:
            rule[match_grp[0][0]] = [int(val) for val in list(match_grp[0])[1:]]
        
        if yourTicketFlag:
            yourTicket = [int(item) for item in line.strip().split(',')]
            yourTicketFlag = False
        if nearbyTicketsFlag:
            nearbyTickets.append([int(item) for item in line.strip().split(',')])
            
        match_grp = re.match(r'^your ticket:$', line.strip())
        if match_grp:
            yourTicketFlag = True
        match_grp = re.match(r'^nearby tickets:$', line.strip())
        if match_grp:
            nearbyTicketsFlag = True
    nearbyTicketsFlag = False
    return rule, yourTicket, nearbyTickets

def rule_check(x, rule):
    #True => No match
    for index in rule:
        if ((x>=rule[index][0]) and (x<=rule[index][1])) or ((x>=rule[index][2]) and (x<=rule[index][3])):
            return False
    return True


def discard_invalid_tickets(rule, nearbyTickets):
    invalid_flag = []
    for i, ticket in enumerate(nearbyTickets):
        ids = [index for index, val in enumerate(map(lambda x: rule_check(x, rule), ticket)) if val]
        if ids:
             invalid_flag.append(True)
        else:
            invalid_flag.append(False)
    valid_tickets = [ticket for i, ticket in enumerate(nearbyTickets) if not invalid_flag[i]]
    return valid_tickets

def discard_invalid_tickets(rule, nearbyTickets):
    invalid_flag = []
    for i, ticket in enumerate(nearbyTickets):
        ids = [index for index, val in enumerate(map(lambda x: rule_check(x, rule), ticket)) if val]
        if ids:
             invalid_flag.append(True)
        else:
            invalid_flag.append(False)
    valid_tickets = [ticket for i, ticket in enumerate(nearbyTickets) if not invalid_flag[i]]
    return valid_tickets

def find_the_rule_dict(rule, nearbyTickets):
    
    valid_tickets = discard_invalid_tickets(rule, nearbyTickets)

    
    rule_dict = {}
    def rule_check_all(rule, indices, num):
        check_result = [] #True means valid for the rule in the index
        for index in np.array(list(rule.keys()))[indices]:
            if ((num>=rule[index][0]) and (num<=rule[index][1])) or ((num>=rule[index][2]) and (num<=rule[index][3])):
                check_result.append(True)
            else:
                check_result.append(False)
        return check_result

    first = True
    for ticket in valid_tickets:
            if first:
                for pos in range(len(ticket)):
                    check_result = rule_check_all(rule, range(len(rule)), ticket[pos])

                    for index,res in enumerate(check_result):
                        if res:
                            rule_dict[index] = rule_dict.get(index, []) + [pos]
                first = False

            else:
                for pos in range(len(ticket)):
                    indices_present = [key for key in rule_dict if pos in rule_dict[key]]
                    check_result = rule_check_all(rule, indices_present, ticket[pos])

                    for index in indices_present:
                        if not check_result[indices_present.index(index)]:
                            existing_pos = rule_dict.get(index, [])
                            existing_pos.remove(pos)
                            rule_dict[index] = existing_pos  
                            
    return rule_dict


def rule_of_elemination(rule_dict, rules, ticket):
    
    index_departure = [index for index, key in enumerate(rules.keys()) if re.match(r'^departure', key)]
    perm = {}
    while rule_dict:
        chosen_options = [option for option in rule_dict if len(rule_dict[option])==1]
        if chosen_options:
            perm[chosen_options[0]]=rule_dict[chosen_options[0]][0]
            del rule_dict[chosen_options[0]]
            for rule in rule_dict:
                val = rule_dict[rule]
                if perm[chosen_options[0]] in val:
                    val.remove(perm[chosen_options[0]])
                    rule_dict[rule]=val
                    
    return reduce(lambda x,y: x*y, [ticket[perm[index]] for index in  index_departure])
 
def part1(rule, nearbyTickets):
    ticket_scanning_error_rate=0
    for ticket in nearbyTickets:
        ids = [index for index, val in enumerate(map(lambda x: rule_check(x, rule), ticket)) if val]
        ticket_scanning_error_rate+=sum([ticket[id] for id in ids])
    return ticket_scanning_error_rate
    
def part2(rule, nearbyTickets, yourTicket):
    rule_dict = find_the_rule_dict(rule, nearbyTickets)
    return rule_of_elemination(rule_dict, rule, yourTicket)

with open('input.txt', 'r') as f:
    file = f.readlines()

rule, yourTicket, nearbyTickets = parse(file)
part1(rule, nearbyTickets)
part2(rule, nearbyTickets, yourTicket)