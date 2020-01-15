from values import rules, inital_facts, queries, facts, implications, bi_implications

def process_lines(file_text):
    global rules
    global inital_facts
    global queries

    # Clean up file.
    for line in file_text:
        # Seperate the rules
        if "=>" in line or "<=>" in line:
            rules.append(line)
        # Seperate the initial facts.
        if line:
            if line[0] == '=':
                inital_facts.append(line)
            if line[0] == '?':
                queries.append(line)


def set_initial_facts():
    global facts
    for query in inital_facts:
        for x in range(len(query) - 1):
            if query[x + 1] != ' ':
                fact = query[x + 1]
                facts[fact] = True
            else:
                break


"""
    Split up the rules into a dictionary that will hold the implicators and the implication.
    
    I.E:
        rules = dict (KEY=implicator: VALUE=implication)
"""
def process_rules(rules):
    for rule in rules:
        if "<=>" in rule:
            tmp_rule = rule.split("<=>")
            if tmp_rule[0].strip() in bi_implications.keys():
                bi_implications[tmp_rule[0].strip()].append(tmp_rule[1].strip())
            else:
                arr = [tmp_rule[1].strip()]
                bi_implications[tmp_rule[0].strip()] = arr 

        elif "=>" in rule:
            tmp_rule = rule.split("=>")
            if tmp_rule[0].strip() in implications.keys():
                implications[tmp_rule[0].strip()].append(tmp_rule[1].strip())
            else:
                arr = [tmp_rule[1].strip()]
                implications[tmp_rule[0].strip()] = arr 



def is_compound(implicator):
    if '+' in implicator or '|' in implicator or '!' in implicator or '^' in implicator:
        return True
    else:
        return False

"""
    Start processsing the rules to determine if a rule is true, false or undertermined.
"""
def work_out_rules():
    global implications
    global facts

    implicators = list(implications.keys())
    implicated = list(implications.values())

    """
        Go though the list of rules and find out if the value of the rule is true.
        so far compound statments are ignored.
    """
    for x in range(len(implicators)):
        if not is_compound(implicators[x]):
            key = facts[implicators[x]]
            if not is_compound(implicated[x][0]):
                facts[implicated[x][0]] = key
            else:
                print("\t\tis compound")
                
        else:
            print("\tis compound.")
