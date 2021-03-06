import re
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


"""
    This is a helper function that checks if a statement is compound or not.

    I.E:
        compound: A + B | D
"""
def is_compound(implicator):
    if '+' in implicator or '|' in implicator or '!' in implicator or '^' in implicator or '(' in implicator:
        return True
    else:
        return False

def propergate(statement):
    global facts
    operators = []
    operands = []
    op1_not = False
    op2_not = False

    # Get all the components.
    components = statement.split(' ')
    for comp in components:
        if comp == '+' or comp == '|' or comp == '^':
            operators.append(comp)
        else:
            operands.append(comp)

    # loop through the operators.
    for operator in operators:
        # print(operands)
        operand_1 = operands.pop(0)
        operand_2 = operands.pop(0)

        if '!' in operand_1:
            op1_not = True
            operand_1 = operand_1[1]
        if '!' in operand_2:
            op2_not = True
            operand_2 = operand_2[1]
        # get the values of the operands
        value_1 = facts[operand_1]
        value_2 = facts[operand_2]

        # Check if the values have a not in them.
        if op1_not:
            value_1 = not value_1
        if op2_not:
            value_2 = not value_2
        print("Operands", operand_1, operand_2)
        print("Ooperators", operator)


        # Process the 'and' operator
        if operator == '+':
            facts["tmp"] = value_1 and value_2
            print("THe value of the result is ", facts['tmp'])
            operands.append('tmp')
        if operator == '|':
            facts['tmp'] = value_1 or value_2
            print("This value might still change", facts['tmp'])
            operands.append('tmp')
        if operator == '^':
            facts['tmp'] = value_1 ^ value_2
            print("The value might stiull change again", facts['tmp'])
            operands.append("tmp")


    return (facts['tmp'])


"""
    Implicated progation.

"""
def imp_prop(statement, value):
    operands = []
    operators = [] 
    set_value = value

    components = statement.split(' ')
    for comp in components:
        if comp == '+' or comp == '|' or comp == '^':
            operators.append(comp)
        else:
            operands.append(comp)

    for operator in operators:
        if operator != '+':
            set_value = 'undefined'
        for op in operands:
            facts[op] = value
        

"""
    Work on substituting the brackets
"""
def sub_brackets(statement):
    global facts
    tmp_str = ""
    add = False
    operands = []
    operators = []
    op1_not = False
    op2_not = False

    for char in statement:
        if char == '(':
            add = True
            continue
        if char == ')':
            break
        if add:
            tmp_str += char
    # Get all the components.
    components = tmp_str.split(' ')
    for comp in components:
        if comp == '+' or comp == '|' or comp == '^':
            operators.append(comp)
        else:
            operands.append(comp)

    for operator in operators:
        # print(operands)
        operand_1 = operands.pop(0)
        operand_2 = operands.pop(0)

        if '!' in operand_1:
            op1_not = True
            operand_1 = operand_1[1]
        if '!' in operand_2:
            op2_not = True
            operand_2 = operand_2[1]
        # get the values of the operands
        value_1 = facts[operand_1]
        value_2 = facts[operand_2]

        # Check if the values have a not in them.
        if op1_not:
            value_1 = not value_1
        if op2_not:
            value_2 = not value_2
        # print("Operands", operand_1, operand_2)
        # print("Ooperators", operator)


        # Process the 'and' operator
        if operator == '+':
            facts["@"] = value_1 and value_2
            print("THe value of the result is ", facts['@'])
            operands.append('@')
        if operator == '|':
            facts['@'] = value_1 or value_2
            print("This value might still change", facts['@'])
            operands.append('@')
        if operator == '^':
            facts['@'] = value_1 ^ value_2
            print("The value might stiull change again", facts['@'])
            operands.append("@")

    print("The value of the bracket is:", facts['@'])
    print(operands)
    print(operators)



"""
    Start processsing the rules to determine if a rule is true, false or undertermined.
    This function only works out 
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
                # facts[implicated[x][0]] = not(key) | facts[implicated[x][0]]
                facts[implicated[x][0]] = key
            else:
                facts[implicated[x][0]] = "undetermind"
                
        else:
            # check if the complex statment has brackets
            if '(' in  implicators[x]:
                print('statement has a bracket')
                sub_brackets(implicators[x])
                implicators[x] = re.sub(r" ?\([^)]+\)", "@", implicators[x])
                print("\timplications:", implicators[x])

                # continue
            # Propegate through the rules.
            value = propergate(implicators[x])

            if not is_compound(implicated[x][0]):
                # facts[implicated[x][0]] = not(value) | facts[implicated[x][0]]
                facts[implicated[x][0]] = value
            else:
                # facts[implicated[x][0]] = 'undefined'
                imp_prop(implicated[x][0], value)


"""
    This function works on the bi-implication.
"""
def work_out_bi():
    global bi_implications
    global facts

    if not bi_implications:
        print("There are no if and only if's")
        return
    implicators = list(bi_implications.keys())
    implicated = list(bi_implications.values())

    for x in range(len(implicators)):
        if not is_compound(implicators[x]):
            key = facts[implicators[x]]
            if not is_compound(implicated[x][0]):
                facts[implicated[x][0]] = key
            else:
                facts[implicated[x][0]] = 'undetermined'
        else:
            if '(' in  implicators[x]:
                print('statement has a bracket')
                sub_brackets(implicators[x])
                implicators[x] = re.sub(r" ?\([^)]+\)", "@", implicators[x])
                print("\timplications:", implicators[x])

                value = propergate(implicated[x])
                if not is_compound(implicated[x][0]):
                    facts[implicated[x][0]] = value
                else:
                    imp_prop(implicated[x][[0]], value)

               
    print(implicators)
    print(implicated)


def answer_q():
    global queries
    global facts

    for x in range(len(queries[0])):
        if queries[0][x] == ' ':
            break
        if queries[0][x] == '?':
            continue
        print(queries[0][x], 'is', facts[queries[0][x]])