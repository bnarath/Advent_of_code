import re
def parse(file):
    rule_dict = {}
    string_list = []
    with open(file, 'r') as f:
        for string in f.readlines():
            if re.match(r'^\d', string):
                index_rule_string = string.split(':')
                rule_combo = index_rule_string[1].strip().split('|')
                try:
                    rule_dict[int(index_rule_string[0])]=[[int(rule) for rule in rules.split()] for rules in rule_combo]
                except:
                    rule_dict[int(index_rule_string[0])] = index_rule_string[1].strip().strip("\"")
            elif string.strip():
                string_list.append(string.strip())
    return rule_dict, string_list
rule_dict, string_list = parse('sample_input.txt')
def cross_concat(a, b):
    if not a and b:
        return b
    elif a and not b:
        return a
    else:
        List = []
        for i in a:
            for j in b:
                List.append(i+j)
        return List
            
def findtherules(id):
    if type(rule_dict[id])==str:
        return [rule_dict[id]]
    else:
        rule_list = []
        for each in rule_dict[id]:
            rules = []
            for seq in each:
                rules = cross_concat(rules,findtherules(seq))
            rule_list = rule_list + rules
        return rule_list
    